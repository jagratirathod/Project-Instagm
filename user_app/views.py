from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from . forms import SignupForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def home(request):
    return render(request, "base.html")

class SignupView(SuccessMessageMixin, CreateView):
    form_class = SignupForm
    template_name = "signup.html"
    success_url = reverse_lazy('user_app:signup')
    success_message = "Successfully signup !"

    def form_valid(self,form):
        response = super().form_valid(form)
        user = form.save()
        subject = 'Welcome to our website'
        message = 'Hi, Thank you for registering.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['jagratirathod02@gmail.com']  
        send_mail( subject, message, email_from, recipient_list )
        return response


class LoginView(CreateView):
    form_class = LoginForm
    template_name = "login.html"
    
    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return redirect("/follow_user/")
        return HttpResponse("You have not signup ! please signup first")


