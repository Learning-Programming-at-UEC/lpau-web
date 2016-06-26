from django.shortcuts import render

from .models import DataFile

def index(request):
    return render(request, 'filemanager/index.html',
                  {'files':DataFile.objects.all(),})


def detail(request, pk):
    try:
        obj = DataFile.objects.get(pk=pk)

    except DataFile.DoesNotExist:
        raise Http404
    return render(request, 'filemanager/detail.html',
                  {'datafile': obj, })
