from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'gnotefront/index.html'


class NotFoundView(TemplateView):
    # 404 view
    template_name = 'gnotefront/404.html'
