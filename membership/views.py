from django.shortcuts import render
from util.views import CommonTemplateView

class IndexView(CommonTemplateView):
    template_name = 'membership/index.html'

class TeachersView(CommonTemplateView):
    template_name = 'membership/teachers.html'
