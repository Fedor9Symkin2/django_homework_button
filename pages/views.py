from django.views.generic import TemplateView


class HomePageVies(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'