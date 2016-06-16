from django.shortcuts import render
from util.views import CommonTemplateView

class IndexView(CommonTemplateView):
    template_name = 'membership/index.html'
