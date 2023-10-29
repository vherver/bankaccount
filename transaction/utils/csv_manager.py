import csv
from datetime import datetime

from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from account.utils.manage_acounts import get_account_id
from transaction.models import Transaction


def create_transactions(transactions):
    invalid_transactions = []
    accounts = {}
    transactions_to_create = []

    for transaction in transactions:
        try:
            email = transaction["account"]
            validate_email(email)
            date = datetime.strptime(transaction["date"], "%Y/%m/%d")

            if email not in accounts:
                accounts[email] = get_account_id(email)

            account_id = accounts[email]

            transactions_to_create.append(
                Transaction(date=date, account_id=account_id, amount=transaction["amount"])
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

    return invalid_transactions


def convert_csv_to_dict(csv_file):
    decoded_file = csv_file.read().decode('utf-8').splitlines()
    csv_data = list(csv.DictReader(decoded_file))
    return csv_data