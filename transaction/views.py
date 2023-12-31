from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from account.utils.manage_comunication import send_account_email
from transaction.models import Transaction
from transaction.utils.csv_manager import (
    create_transactions,
    convert_csv_to_dict,
    validate_transaction_csv_headers,
)


class UploadCSVTemplateView(TemplateView):
    template_name = "index.html"


class UploadCSV(APIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = Transaction.objects.all()
    permission_classes = [AllowAny]

    def post(self, request):
        csv_file = request.data.get("csv_file")
        context = {}
        if csv_file and csv_file.content_type == "text/csv":
            try:
                context["file_loaded"] = True
                transactions = convert_csv_to_dict(csv_file)
                validate_transaction_csv_headers(transactions)
                (
                    context["invalid_transactions"],
                    accounts,
                ) = create_transactions(transactions)
                context.update(send_account_email(accounts))
            except Exception as e:
                context["error"] = e

            return render(request, "index.html", context)

        else:
            context[
                "custom_error"
            ] = "No se proporcionó un archivo CSV válido."  # noqa
            return render(request, "index.html", context)

    def get(self, request):
        context = {"custom_error": "GET no es un metodo valido"}
        return render(request, "index.html", context)
