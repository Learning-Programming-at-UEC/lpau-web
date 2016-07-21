from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import views as auth_views

from . import views

app_name = 'account'
urlpatterns = [
    # /account/login/
    url(r'^login/$', auth_views.login,
        {'template_name': 'accounts/login.html'},
        name='login'),
    # /account/logout/
    url(r'^logout/$', auth_views.logout,
        {'template_name': 'accounts/logged_out.html'},
        name='logout'),
    # /account/password_change/
    url(r'^password_change/$', auth_views.password_change,
        {
            'template_name': 'accounts/password_change.html',
            'post_change_redirect': reverse_lazy('account:password_change_done'),
        },
        name='password_change'),
    # /account/password_change_done/
    url(r'^password_change_done/$', auth_views.password_change_done,
        {'template_name': 'accounts/password_change_done.html'},
        name='password_change_done'),
]
