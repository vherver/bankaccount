from django.views.generic import TemplateView


class MyTemplateView(TemplateView):
    template_name = "index.html"
