from django.views.generic import TemplateView


class Picture1(TemplateView):
    template_name = 'Picture1.html'


class Picture2(TemplateView):
    template_name = 'picture2.html'


class Picture3(TemplateView):
    template_name = 'picture3.html'
