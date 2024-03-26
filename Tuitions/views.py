from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class TuitionView(TemplateView):
    template_name = 'tuitions.html'
