from django import forms
from .models import post


class PostForm(forms.ModelForm): #this helps to creat model forms for our models
    class Meta:
        model = post
        fields =('title', 'title_tag', 'author', 'body')

        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Enter title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            

        }