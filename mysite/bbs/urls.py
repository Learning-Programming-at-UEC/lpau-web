from django.conf.urls import url
from .models import Thread
from django.views.generic import *

from . import views

app_name = "bbs"
urlpatterns = [
    # スレッド一覧のページ
    url(r'^(?P<page>[0-9]+)/$',
        views.IndexView.as_view(),
        {'paginate_by': 5,
         'allow_empty': True, }),
    # トップページ。スレッド一覧のページにリダイレクトする
    url(r'^$', RedirectView.as_view(), {'url': '/1/'}),
    url(r'^thread/new/$', views.ThreadFormView.as_view(), name="form"),
    url(r'^thread/(?P<pk>\d+)/$', views.ThreadDetailView.as_view(), name='thread_detail'),
]
