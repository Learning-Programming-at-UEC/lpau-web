from django.conf.urls import url

from . import views

app_name = 'membership'
urlpatterns = [
    # /membership/
    url(r'^$', views.IndexView.as_view(), {'sidebar': 'index'}, name='index'),
    # /membership/bbs/
    # /membership/download_document/
    url(r'^download_document/', views.DownloadDocumentView.as_view(),
        {'sidebar': 'download_document'}, name='download_document'),
    url(r'^download_file/(?P<date>\w+)/', views.DownloadFileView.as_view(),
        name='download_file'),
    # /membership/schedule/
    # /membership/teachers/
    url(r'^teachers/', views.TeachersView.as_view(), {'sidebar': 'teachers'}, name='teachers'),
    # /membership/example/
]
