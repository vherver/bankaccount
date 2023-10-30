from account.models import Account


def get_account(email: str) -> Account:
    """
    Retrieve or create an Account object based on the provided email.

    Parameters:
    email (str): The email address associated with the Account.

    Description:
    This function attempts to retrieve an existing Account object
    from the database based on the provided email. If the Account
    does not exist, it creates a new Account object and returns it.

    Args:
    - email (str):
     A string representing the email address associated with the Account.

    Returns:
    Account: The Account object associated with the provided email.
    If it doesn't exist, a new Account object is created and returned.

    Type Annotations:
    - email (str): The function expects a string representing an email address.
    - Returns (Account): The function returns an Account object.
    """

    object, _ = Account.objects.get_or_create(email=email)
    return object
