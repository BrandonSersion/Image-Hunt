from django.views.generic.base import TemplateView
from django.shortcuts import render

from .forms import LoginForm
from .forms import SignupForm

# Create your views here.
class LoginView(TempateView):
    def get(self, request):
        login = LoginForm()
        context = {
            "login":login
        }
        return render(request, 'account/login_form.html', context)

    def post(self, request):
        login = LoginForm(request.POST)
        if form.is_valid():
            post = form.cleaned_data['email','password']
        args = {'email':email, 'password':password}
        return render(request, 'account/login_form', args)



class SignupView(TemplateView):
    def get(request):
        signup = SignupForm()
        context = {
            "signup":signup
        }
        return render(request, 'account/signup_form.html', context)
       
    def post(request):
        login = SignupForm(request.POST)
        if form.is_valid():
            post = form.cleaned_data['username','email','password']
        args = {'email':email, 'password':password}
        return render(request, 'account/signup_form', args)