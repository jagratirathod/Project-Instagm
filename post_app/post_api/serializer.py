from rest_framework import serializers
from user_app.models import User
from post_app .models import Post , LikePost


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["user","image","title"]


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["image","title"]


class LikePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikePost
        fields = ["post"]


