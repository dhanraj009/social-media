from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from django.urls import reverse,reverse_lazy
from accounts import forms,views
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required



# Create your views here.
class HomePage(TemplateView):
    template_name = 'index.html'

class SignUp(CreateView):
    form_class = forms.UserCreateForm   
    success_url = reverse_lazy ('login')
    template_name = 'accounts/signup.html'

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name =  "thanks.html"

