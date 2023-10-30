import unittest
from django.test import TestCase
from account.models import Account

from account.utils.manage_acounts import get_account


class TestGetAccount(TestCase):
    def setUp(self):
        self.email = "test@examples.com"
        self.account = Account.objects.create(email=self.email)

    def test_get_existing_account(self):
        retrieved_account = get_account(self.email)
        self.assertEqual(retrieved_account.email, self.email)

    def test_get_non_existing_account(self):
        non_existent_email = "nonexistent@example.com"
        retrieved_account = get_account(non_existent_email)
        self.assertEqual(retrieved_account.email, non_existent_email)


if __name__ == "__main__":
    unittest.main()
