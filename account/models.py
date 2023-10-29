from django.db import models

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
    """

    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

    def __str__(self):
        return self.email
