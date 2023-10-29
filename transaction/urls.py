from django.urls import path

from transaction.views import MyTemplateView

app_name = "transaction"

urlpatterns = [
    path("transaction-list/", MyTemplateView.as_view(), name="mi-endpoint"),
]
