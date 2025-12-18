from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text','photo']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'What\'s on your mind?'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }
class UserRegistrationForm(UserCreationForm):
    email= forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        
        