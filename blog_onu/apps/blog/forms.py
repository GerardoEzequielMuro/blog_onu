from django import forms
from django.forms import ModelForm
from .models import *


class CommentForm(forms.ModelForm):


    class Meta:
        model = Comment
        fields = ('texto',)



