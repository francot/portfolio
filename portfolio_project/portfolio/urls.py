from django.conf.urls import patterns, include, url
from portfolio import views



urlpatterns = patterns(
    'portfolio.views',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<job_url>\w+)/$', views.job, name='job'),
)
