from django.conf.urls import url
from .views import HomeView, NotFoundView

urlpatterns = [
    url(r'^home/$', HomeView.as_view(), name='home'),
    # ToDo: authentication
    url(r'^$', HomeView.as_view()),
    # Stray urls go here
    url(r'^.*/$', NotFoundView.as_view(), name='404'),
]

