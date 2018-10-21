from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^article/1/$', views.article1, name='article1'),
    url(r'^article/2/$', views.article2, name='article2'),
    url(r'^article/3/$', views.article3, name='article3'),
    url(r'^article/4/$', views.article4, name='article4'),
    url(r'^article/5/$', views.article5, name='article5'),
    url(r'^article/6/$', views.article6, name='article6'),
    # url(r'^article/$', views.article, name='article'),
    url(r'^tentang/$', views.tentang, name='tentang')
    # url(r'^jawatimur/$', views.jawatimur, name='jawatimur')
]