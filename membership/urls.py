from django.conf.urls import url
from django.views.generic import RedirectView

from . import views


app_name = 'membership'
urlpatterns = [
    # /membership/
    url(r'^$', views.IndexView.as_view(), {'sidebar': 'index'}, name='index'),
    # /membership/student_work
    url(r'^student_work/$', views.StudentWorkView.as_view(),
        {'sidebar': 'student_work'}, name='student_work'),
    # /membership/bbs/<pk>/
    url(r'^bbs/$', RedirectView.as_view(url='1/')),
    url(r'^bbs/(?P<pk>\d+)/$', views.ThreadView.as_view(),
        {'sidebar': 'bbs'}, name='bbs'),
    # /membership/download_document/
    url(r'^download_document/$', views.DownloadDocumentView.as_view(),
        {'sidebar': 'download_document'}, name='download_document'),
    url(r'^download_file/(?P<difficulty>\w+)/(?P<date>\d+)/$', views.DownloadFileView.as_view(),
        name='download_file'),
    # /membership/schedule/
    # /membership/teachers/
    url(r'^teachers/$', views.TeachersView.as_view(),
        {'sidebar': 'teachers'}, name='teachers'),
    # /membership/example/
]
