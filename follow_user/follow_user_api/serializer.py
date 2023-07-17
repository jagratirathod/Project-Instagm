from rest_framework import serializers
from user_app.models import User
from follow_user .models import SendRequest


class AllUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email" , "first_name" , "last_name"]

        
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendRequest
        fields = ["status","user","sender","receive"]

class RequestDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendRequest
        fields = ["status","user","sender","receive"]

class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email","first_name" , "last_name","images"]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email","first_name" , "last_name","images"]
