from django.db import models

from backaccount.mixins.models import TimeStampMixin


class Transaction(TimeStampMixin):
    """
       Represents a financial transaction in the application.

       This model represents a financial transaction, including information about the transaction amount, date, and the associated bank account.

       Attributes:
           amount (DecimalField): The amount of the transaction, with a maximum of 20 digits and 2 decimal places.
           date (DateField): The date when the transaction occurred.
           account (OneToOneField): A reference to the bank account involved in the transaction. The associated account will be deleted when the transaction is deleted (CASCADE).

       Meta:
           verbose_name = "Transaction"
           verbose_name_plural = "Transactions"


       Inheritance:
           This model inherits timestamp fields (created, updated, and deleted) from the TimeStampMixin.

       Dependencies:
           This model relies on the Account model from the "account" app, which is imported at the top of this file.

       """

    amount = models.DecimalField(
        max_digits=20,
        decimal_places=2
    )
    date = models.DateField()

    account = models.OneToOneField("account.Account", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"