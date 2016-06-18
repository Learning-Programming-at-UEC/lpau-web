from django.conf.urls import url

from . import views

app_name = 'membership'
urlpatterns = [
    # /membership/
    url(r'^$', views.IndexView.as_view(), {'sidebar': 'index'}, name='index'),
    # /membership/bbs/
    # /membership/schedule/
    # /membership/teachers/
    url(r'^teachers/', views.TeachersView.as_view(), {'sidebar': 'teachers'}, name='teachers'),
    # /membership/example/
]
