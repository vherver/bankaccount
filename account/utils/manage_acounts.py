from account.models import Account


def get_account_id(email):
    object, _ = Account.objects.get_or_create(email=email)
    return object.id