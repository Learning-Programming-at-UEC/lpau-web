from django.conf.urls import url

from . import views

app_name = 'membership'
urlpatterns = [
    # /membership/
    url(r'^$', views.IndexView.as_view(), name='index'),
]
