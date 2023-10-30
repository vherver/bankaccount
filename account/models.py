import calendar

from _decimal import Decimal
from django.db import models
from django.db.models import Sum, Avg, Count
from django.db.models.functions import ExtractMonth, ExtractYear

from backaccount.mixins.models import TimeStampMixin


class Account(TimeStampMixin):
    """
    Represents a back account in the application.

    Attributes:
        email (EmailField):
        A unique email address associated with the user account.

    Inheritance:
    This model inherits timestamp fields (created, updated, and deleted)
    from the TimeStampMixin.

    Methods:
    - get_balance(self): Returns the total balance of the account
       based on its transactions.
    - get_credit_average(self): Returns the average of credit
       transactions for the account.
    - get_debit_average(self): Returns the average of debit
      transactions for the account.
    - get_month_transactions(self): Returns a list of monthly
      transaction counts for the account.
    """

    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

    def __str__(self):
        return self.email

    def get_balance(self):
        return (
            self.transactions.all()
            .aggregate(total_sum=Sum("amount"))["total_sum"]
            .quantize(Decimal("0.00"))
        )

    def get_credit_average(self):
        return (
            self.transactions.filter(amount__gte=0)
            .aggregate(total_sum=Avg("amount"))["total_sum"]
            .quantize(Decimal("0.00"))
        )

    def get_debit_average(self):
        return (
            self.transactions.filter(amount__lte=0)
            .aggregate(total_sum=Avg("amount"))["total_sum"]
            .quantize(Decimal("0.00"))
        )

    def get_month_transactions(self):
        events = (
            self.transactions.annotate(
                month=ExtractMonth("date"),
                year=ExtractYear("date"),
            )
            .values("month", "year")
            .annotate(transactions=Count("id"))
            .order_by("month")
        )

        for event in events:
            event["name"] = calendar.month_name[event["month"]]

        return events
