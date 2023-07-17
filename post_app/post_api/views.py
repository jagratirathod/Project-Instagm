from rest_framework .views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView , CreateAPIView
from post_app.models import Post , LikePost
from .serializer import PostSerializer , CreatePostSerializer , LikePostSerializer
from django.db.models import Q
from follow_user.models import SendRequest 
from django.utils.timezone import make_aware
from datetime import datetime


# Create your views here.

class CheckPostAPI(APIView):
    def get(self,request):
        return Response("check post api......")

class ListPostView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        start_date = self.request.GET.get("start_date")
        end_date  =  self.request.GET.get("end_date")

        if start_date and end_date:
            start_date = make_aware(datetime.strptime(start_date, "%Y-%m-%d"))
            end_date = make_aware(datetime.strptime(end_date, "%Y-%m-%d"))
            post = Post.objects.filter(user=self.request.user, created_at__range=[start_date, end_date])
            return post
        else:
            senders_post = SendRequest.objects.filter(user=self.request.user, status="Following").values_list('sender')
            users = Post.objects.filter(Q(user=self.request.user) | Q(user__in=senders_post))
            return users


class CreatePostview(CreateAPIView):
    # localhost:8000/api_post/create_post/
    queryset = Post
    serializer_class = CreatePostSerializer

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )


class LikePostView(APIView):
    def get(self,request):
        post_id  =  self.request.GET.get("post_id")
        post = Post.objects.get(id = post_id)

        like_post = LikePost.objects.filter(post = post , like_by = self.request.user)
        if not like_post:
            LikePost.objects.create(post = post , like_by = self.request.user,number_of_likes = 1)
            return Response("Successfully Like Post")








    





        







          

