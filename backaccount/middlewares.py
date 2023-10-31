from django.urls import resolve
from django.shortcuts import redirect

class Middleware404:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404:
            return redirect('transaction:index')
        return response
