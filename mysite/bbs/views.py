from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.models import User

from .models import Thread, Comment
from .forms import CommentForm


class IndexView(generic.ListView):
    # template_name = 'bbs/thread_list.html'
    context_object_name = 'Thread_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Thread.objects.all().order_by('-id')


class ThreadFormView(generic.edit.CreateView):
    model = Thread
    fields = ['title', 'message']


class ThreadView(generic.FormView, generic.DetailView):
    model = Thread
    template_name = "bbs/thread.html"
    form_class = CommentForm
    success_url = './'

    def get_context_data(self, **kwargs):
        # 表示するスレッド
        context = super(generic.FormView, self).get_context_data(**kwargs)
        thread = get_object_or_404(Thread, pk=self.kwargs.get(self.pk_url_kwarg))
        context['comment_list'] = thread.comment_set.all().order_by('id')
        return context

    def form_valid(self, form):
        form.instance.username = self.request.user.username
        form.instance.thread = get_object_or_404(Thread, pk=self.kwargs.get(self.pk_url_kwarg))
        form.instance.save()
        return super(ThreadView, self).form_valid(form)
