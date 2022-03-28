from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"

class Dashboard(TemplateView):
    template_name = "dashboard.html"