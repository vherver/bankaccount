from account.models import Account

def create_missing_accounts(accounts_to_consult):
    accounts_in_db = Account.objects.filter(email__in=accounts_to_consult).values_list("email", flat=True)
    missing_accounts = accounts_to_consult - set(accounts_in_db)

    accounts_to_create = (Account(email=missing_account) for missing_account in missing_accounts)
    Account.objects.bulk_create(accounts_to_create)


def get_account_id(email):
    object, _ = Account.objects.get_or_create(email=email)
    return object.id