import json

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic import View
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.utils.decorators import classonlymethod


class LoginRequiredViewMixin(object):
    """
    ログインが必要なViewのMixin
    """
    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredViewMixin, cls).as_view(**initkwargs)
        view = login_required(view)
        return view


class CommonTemplateView(LoginRequiredViewMixin, TemplateView):
    pass


class CommonListView(LoginRequiredViewMixin, ListView):
    pass


class CommonCreateView(LoginRequiredViewMixin, CreateView):
    pass


class CommonUpdateView(LoginRequiredViewMixin, UpdateView):
    pass


class CommonDeleteView(LoginRequiredViewMixin, DeleteView):
    pass


class CommonDetailView(LoginRequiredViewMixin, DetailView):
    pass


# class CommonWizardView(LoginRequiredViewMixin, SessionWizardView):
#     pass


class CommonAjaxView(LoginRequiredViewMixin, View):
    def dict_to_json_response(self, dict_data, status_code=200):
        ret = json.dumps(dict_data, ensure_ascii=False)
        response = HttpResponse(ret, content_type='application/json', status=status_code)
        return response
