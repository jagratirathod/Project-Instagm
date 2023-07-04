from django import forms
from .models import Post  ,CommentPost


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'title']



class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = CommentPost
        fields = ['message']
