from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from util.views import CommonView
from util.views import CommonTemplateView
from django.views.generic import FormView
from util.views import CommonDetailView
from util.views import CommonListView

from .models import Thread, Comment
from .forms import CommentForm


class IndexView(CommonTemplateView):
    template_name = 'membership/index.html'

class TeachersView(CommonTemplateView):
    template_name = 'membership/teachers.html'

class ThreadView(FormView, CommonDetailView):
    template_name = 'membership/thread.html'
    model = Thread
    form_class = CommentForm
    success_url = './'

    def get_context_data(self, **kwargs):
        # 表示するスレッド
        context = super(FormView, self).get_context_data(**kwargs)
        thread = get_object_or_404(Thread, pk=self.kwargs.get(self.pk_url_kwarg))
        context['comment_list'] = thread.comment_set.all().order_by('id')

        return context

    def form_valid(self, form):
        form.instance.username = self.request.user.username
        form.instance.thread = get_object_or_404(Thread, pk=self.kwargs.get(self.pk_url_kwarg))
        form.instance.save()

        return super(ThreadView, self).form_valid(form)


# 講義資料リスト: linkは django_project_root/files/documents/ の中を指している
document_list = [
    {'file_name': 'lpau_20160508.pptx', 'link': '1.pptx', 'date': '20160508'},
    {'file_name': 'lpau_20160512.pptx', 'link': '2.pptx', 'date': '20160512'},
    {'file_name': 'lpau_20160522.pptx', 'link': '3.pptx', 'date': '20160522'},
    {'file_name': 'lpau_20160529.pptx', 'link': '4.pptx', 'date': '20160529'},
    {'file_name': 'lpau_20160605.pptx', 'link': '5.pptx', 'date': '20160605'},
    {'file_name': 'lpau_20160612.pptx', 'link': '6.pptx', 'date': '20160612'},
    {'file_name': 'lpau_20160619.pptx', 'link': '7.pptx', 'date': '20160619'},
]

class DownloadDocumentView(CommonListView):
    template_name = 'membership/download_document.html'
    context_object_name = 'document_list'

    def get_queryset(self):
        return document_list

class DownloadFileView(CommonView):
    def get(self, request, *args, **kwargs):
        date = kwargs['date']
        for document in document_list:
            if document['date'] == date:
                link = document['link']
                file_name = document['file_name']

        response = HttpResponse(
            open('files/documents/' + link, 'rb').read(),
            content_type='application/octet-stream'
        )
        response['Content-Disposition'] = 'attachment; filename = "' + file_name + '"'

        return response
