from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^tentang/$', views.tentang, name='tentang'),
    # url(r'^jawatimur/$', views.jawatimur, name='jawatimur')
]