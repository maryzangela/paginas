from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    template = loader.get_template('templates/home.html')
    contex = { 'var': var,}
    return HttpResponse(template.render(context, request))

def homePageView(request):
    return HttpResponse('Hello, Words!')

class HomePageView(TemplateView):
    template_name = 'home.html'

class SobrePageView(TemplateView):
    template_name = 'sobre.html'

def index(request):

context = {'var': var}
return render(request, 'templates/home.html', context)

# Create your views here.
