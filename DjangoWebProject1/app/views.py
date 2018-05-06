"""
Definition of views.
"""
from django.template import RequestContext
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .forms import HomeForm

class HomeView(TemplateView):
 template_name = 'app/index.html'

def get(self,request):
    if request.method == 'POST':
     form=HomeForm(request.Post)
    if form.is_valid():
     return HttpResponseRedirect('/thanks/')
    else:
        form = HomeForm()
    return render(request,template_name,{'form':form})

def index(request):
    return render(request, 'app/layout.html')

def output(request):
    if request.is_ajax():
        py_obj = tuningalgo
        return render(request, 'app/output.html', {'output': py_obj})

