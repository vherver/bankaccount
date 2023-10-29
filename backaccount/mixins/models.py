from django.db import models


class TimeStampMixin(models.Model):
    """
    A mixin to add timestamp fields to a model, allowing you to track
    when records were created, updated, and optionally deleted.

    Attributes:
        created (DateTimeField):
            The datetime when the record was created, automatically
            set to the current time when a new record is added.
        updated (DateTimeField):
            The datetime when the record was last updated, automatically
            updated to the current time when the record was modified.
        deleted (DateTimeField, optional):
            The datetime when the record was soft-deleted, set to None by
            default. Use it to track when a record was deleted without
            physically removing it from the database.

    Meta:
        abstract = True

    Example:
        To use the `TimeStampMixin` in a model, simply inherit from it:
        ```python
        class MyModel(TimeStampMixin):
            name = models.CharField(max_length=100)
            # Other fields for your model
        ```
    """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(default=None, blank=True, null=True)

    class Meta:
        abstract = True
