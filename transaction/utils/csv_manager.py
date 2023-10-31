import csv
from datetime import datetime

from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from account.utils.manage_acounts import get_account
from transaction.models import Transaction


def create_transactions(transactions):
    """
    Create transactions and associate them with user accounts.

    Parameters:
    transactions (list):
    A list of transaction data to be processed and saved.

    Returns:
    tuple:
    A tuple containing two lists - invalid_transactions and accounts.
        - invalid_transactions (list): A list of transactions that
          could not be processed due to errors.
        - accounts (dict): A dictionary of user accounts used to
          associate transactions.

    Description:
    This function processes a list of transactions, validates it, and
    creates new Transaction objects in the database. Each transaction
    is associated with a user account identified by their email address.
    Any invalid transactions are collected in the 'invalid_transactions'
    list, and a 'accounts' dictionary is populated with associated accounts.

    Example Usage:
    transactions = [
        {
            "account": "user1@example.com",
            "date": "2023/10/29",
            "amount": 100.50
        }
    ]

    Notes:
    - The 'date' parameter should be in the format "%Y/%m/%d".
    - Invalid transactions are those that cannot be processed
      due to validation errors and are included in 'invalid_transactions'.
    """

    invalid_transactions = []
    accounts = {}
    transactions_to_create = []

    for transaction in transactions:
        try:
            email = transaction["account"]
            validate_email(email)
            date = datetime.strptime(transaction["date"], "%Y/%m/%d")

            if email not in accounts:
                accounts[email] = get_account(email)

            account = accounts[email]

            transactions_to_create.append(
                Transaction(
                    date=date, account=account, amount=transaction["amount"]
                )
            )
        except ValidationError as e:
            transaction["error"] = e.message
            invalid_transactions.append(transaction)
            continue
        except ValueError as e:
            transaction["error"] = e
            invalid_transactions.append(transaction)
            continue

    Transaction.objects.bulk_create(transactions_to_create)

    return invalid_transactions, accounts


def convert_csv_to_dict(csv_file):
    decoded_file = csv_file.read().decode("utf-8").splitlines()
    csv_data = list(csv.DictReader(decoded_file))
    return csv_data


def validate_transaction_csv_headers(dict_csv):
    if len(dict_csv) > 0 and (
        set(["account", "date", "amount"]) - set(dict_csv[0].keys())
    ):
        raise ValueError(
            "Los encabezados del csv no son correctos, "
            "verificarlos (account, date, amount)"
        )
