from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.list import ListView
from project_instagram import settings
from user_app.models import User
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from .forms import UserProfileUpdateForm
from .models import SendRequest, User

# Create your views here.

def home(request):
    return render(request, "f_base.html")

class AllUser(ListView):
    model = User
    context_object_name = "users"
    template_name = "all_user.html"

    def get_queryset(self):
        users = User.objects.filter(
            ~Q(is_staff=True), ~Q(email=self.request.user))

        followed_users = SendRequest.objects.filter(
            user=self.request.user).values_list('sender__email', flat=True)

        if followed_users:
            users = users.filter(
                ~Q(send__user__email__in=followed_users))
            return users
        return users


class Notification(ListView):
    model = User
    context_object_name = "users"
    template_name = "notifications.html"

    def get_queryset(self):
        users = SendRequest.objects.filter(
            user=self.request.user)
        return users


def update_status(request):
    user_id = request.GET.get("user")
    user = User.objects.get(id=user_id)
    users = SendRequest.objects.create(user=user, receive=request.user)
    users = SendRequest.objects.create(user=request.user, sender=user)
    return redirect('follow_user:user')


def start_following(request):
    user_id = request.GET.get("user")
    sender = request.GET.get("sender")

    # Update the status of the opposite user to "Following"
    receive_email= SendRequest.objects.filter(id= user_id).values_list('receive__email',flat=True)
    update_opposite_user = SendRequest.objects.filter(user__email__in = receive_email , status = "Requested" , sender = request.user).update(
        status=SendRequest.STATUS_TYPE_CHOICES[1][0])
    
        # Update the status of the current user to "Accept"
    update_current_user = SendRequest.objects.filter(id=sender).update(status=SendRequest.STATUS_TYPE_CHOICES[5][0])
    return redirect("follow_user:user")


class Requestdelete(DeleteView):
    model = SendRequest
    template_name = "request_delete.html"
    success_url = reverse_lazy("follow_user:notification")

    def get_object(self, queryset=None, *args, **kwargs):
        user_id = self.kwargs['pk']
        del_request_id = SendRequest.objects.filter(id = user_id).values_list('receive')
        sender_del = SendRequest.objects.filter(user__in= del_request_id,status= "Requested",sender__email= self.request.user.email)
        sender_del.delete()
        return super().get_object(queryset)

# --------------------------------------------------------------------------------------------

def profile(request):
    return render(request, 'profile.html')


class ProfileUpdateView(LoginRequiredMixin,SuccessMessageMixin, UpdateView):
    login_url = settings.login_url
    form_class = UserProfileUpdateForm
    model = User
    template_name = 'profile-update.html'
    success_url = reverse_lazy("follow_user:profile")
    success_message = "Successfully Edit Profile..."


class SeeUserProfileView(ListView):
    model  = User
    context_object_name = "profile"
    template_name = "see_user_profile.html"
    
    def get_queryset(self):
        user_id =  self.request.GET.get("user")
        return User.objects.get(id=user_id)

# -----------------------------------------------------------------------
  
def changepassword(request):
    if request.method == "POST":
        email =  request.POST.get("email")
        password = request.POST.get("password")
        new_password = request.POST.get("new_password")
        user = User.objects.get(email = email)
        if user:
            if check_password(password, user.password):          
                user.set_password(new_password)
                user.save()
                return HttpResponse("Successfully change password")
            return HttpResponse("Password is not correct")

        return HttpResponse("User does not exists")
    else:
        return render(request,"changepasswords.html",{"message":"Successfully change password"})


