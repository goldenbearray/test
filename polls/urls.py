from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^query/$', views.query, name='query'),
    url(r'^detail/(?P<text>[A-Za-z0-9\.\'$,\-\s]+)/$', views.detail, name='detail'),
    url(r'^check.html', views.query, name='query'),
    url(r'^about.html', views.about, name='about'),
    url(r'^base.html', views.index, name='index'),
]