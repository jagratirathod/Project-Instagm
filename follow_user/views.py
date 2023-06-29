from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from user_app.models import User
from . models import SendRequest, Post
from django.db.models import Q
from django.http import HttpResponse
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .forms import PostForm
from django. contrib import messages

# Create your views here.


def home(request):
    return render(request, "f_base.html")


class PostList(ListView):
    model = Post
    template_name = "users_post.html"
    context_object_name = "user_post"

    def get_queryset(self):
        senders_post = SendRequest.objects.filter(user = self.request.user,status="Following").values_list('sender')
        users = Post.objects.filter(
            Q(user=self.request.user) | Q(user__in = senders_post))
        return users


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
    user_email = request.GET.get("user")
    sender = request.GET.get("sender")
    opposite_user_id = SendRequest.objects.filter(
        user__email=user_email).values_list('id', flat=True).last()
    # Update the status of the opposite user to "Following"
    update_opposite_user = SendRequest.objects.filter(id=opposite_user_id).update(
        status=SendRequest.STATUS_TYPE_CHOICES[1][0])
    # Update the status of the current user to "Accept"
    update_current_user = SendRequest.objects.filter(id=sender).update(
        status=SendRequest.STATUS_TYPE_CHOICES[5][0])
    return redirect("follow_user:user")


class Requestdelete(DeleteView):
    model = SendRequest
    template_name = "request_delete.html"
    success_url = reverse_lazy("follow_user:notification")


def PostView(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form = form.save()
            return messages.success(request, "Successfully created")
    else:
        form = PostForm()
        return render(request, "post.html", {"form": form})
