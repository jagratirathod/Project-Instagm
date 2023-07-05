from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from follow_user.models import SendRequest

from .forms import CreateCommentForm, PostForm
from .models import CommentPost, LikePost, Post

# Create your views here.


def home(request):
    return HttpResponse("post testing")


class ListPostView(ListView):
    model = Post
    template_name = "users_post.html"
    context_object_name = "user_post"

    def get_queryset(self):
        senders_post = SendRequest.objects.filter(user = self.request.user,status="Following").values_list('sender')
        users = Post.objects.filter(
            Q(user=self.request.user) | Q(user__in = senders_post))
        return users

def CreatePostView(request):
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


def LikePostView(request): 
    id = request.GET.get("post_id")
    post_id = Post.objects.get(id=id)
    if post_id:
        like_post = LikePost.objects.filter(user=request.user, post = post_id).last()
        if not like_post:
            like = LikePost.objects.create(user=request.user, post = post_id,number_of_likes = 1)
            return redirect("post_app:list_post")
        return HttpResponse("Already liked this Post")


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


class Postdelete(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("post_app:list_post")
