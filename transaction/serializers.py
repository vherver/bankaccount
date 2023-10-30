from rest_framework import serializers


class CSVFileSerializer(serializers.Serializer):
    csv_file = serializers.FileField()
