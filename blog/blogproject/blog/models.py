from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now()) #default- when you create post it will be the time and also let it that if you want with more code you cna edit the time so its not hardcoded in
    author = models.ForeignKey(User, on_delete=models.CASCADE) #author can have many posts - one to many.  cascade- user is deleted so will the post be deleted

    def __str__(self): #string in the shell
        return self.title