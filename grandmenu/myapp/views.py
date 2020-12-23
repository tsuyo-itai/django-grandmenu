from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic

# Create your views here.
class Home(generic.TemplateView):
    template_name = 'myapp/home.html'