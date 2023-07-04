from django import forms
from user_app. models import User


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ("images","email","first_name","last_name")