from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from . import models

# Create your views here.


class index(TemplateView):

    template_name = 'index.html'


class StudentCreateView(CreateView):
    model = models.Student
    fields = ['name', 'age', 'course']
    template_name = 'CreateStudent.html'

    success_url = '/thanku/'


class Thanku(TemplateView):

    template_name = 'Thanks.html'