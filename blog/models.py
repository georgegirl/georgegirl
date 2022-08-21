
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class post(models.Model):
    title= models.CharField(max_length= 255)
    title_tag= models.CharField(max_length= 255, default="SEACHANGE")#this provides a tag wen opening a post, if given a specific title tag  default which is seachange.
    author= models.ForeignKey(User, on_delete=models.CASCADE) #this helps to delete the post of an author in the admin page
    body= models.TextField()
    Post_date = models.DateField(auto_now_add=True)

    

    def __str__(self):
        return self.title + ' | ' + str(self.author) #this would allow us at the admin page to see the title of the blog page and the author.

    def get_absolute_url(self):
        return reverse('article-detail', args=(str(self.id)))
        # return reverse('home')