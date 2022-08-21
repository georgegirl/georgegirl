from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import post
from .forms import PostForm

class HomeView(ListView):
    model = post 
    template_name= 'home.html'

class ArticleDetailView(DetailView):
    model = post
    template_name= 'article_detail.html'

class AddPostView(CreateView):
    model = post
    # fields='__all__'
    template_name ='add-post.html'
    form_class = PostForm

