from typing import Any
from django.db.models import Q
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from follow_user.models import SendRequest
from django.views import View
from .forms import CreateCommentForm, PostForm
from .models import CommentPost, LikePost, Post
from django.utils.timezone import make_aware
from datetime import datetime
from django.db.models import F
from user_app.models import User
from django.db.models import Sum


# Create your views here.

def home(request):
    return HttpResponse("post testing")

class ListPostView(ListView):
    model = Post
    template_name = "users_post.html"
    context_object_name = "user_post"

    def get_queryset(self):
        start_date = self.request.GET.get("start_date")
        end_date = self.request.GET.get("end_date")
        if start_date and end_date:
            start_date = make_aware(datetime.strptime(start_date, "%Y-%m-%d"))
            end_date = make_aware(datetime.strptime(end_date, "%Y-%m-%d"))
            post = Post.objects.filter(user=self.request.user, created_at__range=[start_date, end_date])
            return post
        else:
            senders_post = SendRequest.objects.filter(user=self.request.user, status="Following").values_list('sender')
            users = Post.objects.filter(Q(user=self.request.user) | Q(user__in=senders_post))
            return users
        
    # def post(self, request, *args, **kwargs):
    #     return self.get(request, *args, **kwargs)

def createpostview(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form = form.save()
            return redirect("post_app:list_post")
        else:
            return HttpResponse("Form is not valid") 
    else:
        form = PostForm()
        return render(request, "post.html", {"form": form})


class LikePostView(View):
    def get(self, request):
        post_id = request.GET.get("post_id")
        post = Post.objects.get(id=post_id)
        like = LikePost.objects.filter(post = post , like_by = request.user)
        if not like:
            LikePost.objects.create(post = post , like_by = request.user,number_of_likes = 1)
            return redirect("post_app:list_post")
        return HttpResponse("Already liked")
    

class CreateCommentView(CreateView):
    form_class = CreateCommentForm
    template_name = "comment.html"
    success_url = reverse_lazy('post_app:list_post')
    success_message = "Successfully  Comment"

    def form_valid(self, form):
        post_id = self.request.GET.get("post_id")
        post_id = Post.objects.get(id=post_id)
        form.instance.user = self.request.user
        form.instance.post = post_id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = self.request.GET.get("post_id")
        post_id = Post.objects.get(id=post_id)
        context['post_message'] = CommentPost.objects.filter(post = post_id)
        return context

class PostDelete(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("post_app:list_post")


class PostSortView(View):
    def get(self,request):
        sort = request.GET.get('sort')
        like_post =  Post.objects.filter(user=request.user)
        if sort == "LTH":
            user_post = like_post.order_by('like__number_of_likes')
        else:
            user_post = like_post.order_by('-like__number_of_likes')
        return render(request, 'users_post.html', {'user_post': user_post})
    


        







