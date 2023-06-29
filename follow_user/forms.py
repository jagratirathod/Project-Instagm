from django import forms
from follow_user . models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'title']
