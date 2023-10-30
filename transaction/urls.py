from django.urls import path

from transaction.views import UploadCSVTemplateView, UploadCSV

app_name = "transaction"

urlpatterns = [
    path("", UploadCSVTemplateView.as_view(), name="mi-endpoint"),
    path("upload-csv/", UploadCSV.as_view(), name="upload-csv"),
]
