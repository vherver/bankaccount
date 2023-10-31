from django.conf import settings

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_account_email(accounts):
    """
    Sends summary state of account emails to the specified accounts.

    Parameters:
    accounts (dict): A dictionary containing account information.

    Description:
    This function takes a dictionary of accounts and sends personalized
    emails with a summary of the account's state to the email addresses
    associated with each account. The details of the summary include the
    balance, average credits, average debits,
    and a list of monthly transactions.

    Example Usage:
    accounts_data = {
        {'vicherver@gmail.com': <Account: vicherver@gmail.com>}
    }

    send_account_email(accounts_data)

    External Dependencies:
    - SendGrid: This function uses SendGrid to send emails.
      Ensure that you configure API keys and email templates
      in your SendGrid settings.
    """

    messages_data = {"sending_errors": []}
    if not (
        settings.SENDGRID_FROM_EMAIL
        and settings.SENDGRID_TEMPLATE_ID
        and settings.SENDGRID_API_KEY
    ):
        messages_data[
            "custom_error"
        ] = "Sendgrid no esta configurado correctamente"

    for account in accounts:
        account = accounts[account]
        data = {
            "email": account.email,
            "balance": "$ {:.2f}".format(account.get_balance()),
            "avg_credit": "$ {:.2f}".format(account.get_credit_average()),
            "avg_debit": "$ {:.2f}".format(account.get_debit_average()),
            "months": list(account.get_month_transactions()),
        }

        message = Mail(
            from_email=settings.SENDGRID_FROM_EMAIL,
            to_emails=account.email,
            subject="Resumen Estado de cuenta",
        )

        message.dynamic_template_data = data
        message.template_id = settings.SENDGRID_TEMPLATE_ID

        try:
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(message)
        except Exception as e:
            messages_data["sending_errors"].append(
                {"email": account.email, "reason": e}
            )

    return messages_data
