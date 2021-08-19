from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Comment

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'user', 'project']
