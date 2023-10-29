import csv
from datetime import datetime

from account.utils.manage_acounts import create_missing_accounts, get_account_id
from transaction.models import Transaction


def create_transactions(transactions):
    accounts = {}
    transactions_to_create = []

    for transaction in transactions:
        if transaction["account"] not in accounts:
            accounts[transaction["account"]] = get_account_id(transaction["account"])

        account_id = accounts[transaction["account"]]
        date = datetime.strptime(transaction["date"], "%Y/%m/%d")
        transactions_to_create.append(
            Transaction(date=date, account_id=account_id, amount=transaction["amount"])
        )

    Transaction.objects.bulk_create(transactions_to_create)


    return


def convert_csv_to_dict(csv_file):
    decoded_file = csv_file.read().decode('utf-8').splitlines()
    csv_data = list(csv.DictReader(decoded_file))
    return csv_data