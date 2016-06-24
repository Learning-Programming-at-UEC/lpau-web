from django.http import HttpResponse
from util.views import CommonTemplateView
from util.views import CommonListView
from util.views import CommonView


class IndexView(CommonTemplateView):
    template_name = 'membership/index.html'

class TeachersView(CommonTemplateView):
    template_name = 'membership/teachers.html'


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
