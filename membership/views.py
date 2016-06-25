from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from util.views import CommonView
from util.views import CommonTemplateView
from django.views.generic import FormView
from util.views import CommonDetailView
from util.views import CommonListView
from datetime import datetime

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
# TODO: 表示時に順番が逆転してしまう可能性有
document_list = {
    'entry': [
        {'file_name': 'lpau_entry1_20160508.pptx', 'link': '1.pptx',
            'date': '20160508', 'datetime': datetime(2016, 5, 8)},
        {'file_name': 'lpau_entry2_20160512.pptx', 'link': '2.pptx',
            'date': '20160512', 'datetime': datetime(2016, 5, 12)},
        {'file_name': 'lpau_entry3_20160522.pptx', 'link': '3.pptx',
            'date': '20160522', 'datetime': datetime(2016, 5, 22)},
        {'file_name': 'lpau_entry4_20160529.pptx', 'link': '4.pptx',
            'date': '20160529', 'datetime': datetime(2016, 5, 29)},
        {'file_name': 'lpau_entry5_20160605.pptx', 'link': '5.pptx',
            'date': '20160605', 'datetime': datetime(2016, 6, 5)},
        {'file_name': 'lpau_entry6_20160612.pptx', 'link': '6.pptx',
            'date': '20160612', 'datetime': datetime(2016, 6, 12)},
        {'file_name': 'lpau_entry7_20160619.pptx', 'link': '7.pptx',
            'date': '20160619', 'datetime': datetime(2016, 6, 19)},
    ],
    'basic': [
        {'file_name': 'lpau_basic1_20160522.pdf', 'link': '1.pdf',
            'date': '20160522', 'datetime': datetime(2016, 5, 22)},
        {'file_name': 'lpau_basic2_20160529.pdf', 'link': '2.pdf',
            'date': '20160529', 'datetime': datetime(2016, 5, 29)},
        {'file_name': 'lpau_basic3_20160605.pdf', 'link': '3.pdf',
            'date': '20160605', 'datetime': datetime(2016, 6, 5)},
        {'file_name': 'lpau_basic4_20160619.pdf', 'link': '4.pdf',
            'date': '20160619', 'datetime': datetime(2016, 6, 19)},
    ],
}

class DownloadDocumentView(CommonListView):
    template_name = 'membership/download_document.html'
    context_object_name = 'document_list'

    def get_queryset(self):
        return document_list

class DownloadFileView(CommonView):
    def get(self, request, *args, **kwargs):
        date = kwargs['date']
        difficulty = kwargs['difficulty']
        for document in document_list[difficulty]:
            if document['date'] == date:
                link = document['link']
                file_name = document['file_name']

        response = HttpResponse(
            open('files/documents/' + difficulty + link, 'rb').read(),
            content_type='application/octet-stream'
        )
        response['Content-Disposition'] = 'attachment; filename = "' + file_name + '"'

        return response
