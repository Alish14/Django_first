from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=225)
    def __str__(self):
        return self.name

class Post(models.Model):
    image=models.ImageField(upload_to='blog/',default='blog/default.jpg')
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title=models.CharField(max_length=300)
    content=models.TextField()
    contact_views=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    published_date=models.DateTimeField(null=True)
    created_date=models.DateField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    category=models.ManyToManyField(Category)
    tags = TaggableManager()

    def __str__(self):
        return self.title
    class Meta:
        ordering=['created_date']
    def get_absolute_url(self):
        return reverse('blog:single',kwargs={'pid':self.id})
class comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    name=models.CharField(max_length=225)
    email=models.EmailField()
    subject=models.CharField(max_length=225,blank = True)
    message=models.TextField()
    created_date=models.DateField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    approved=models.BooleanField(default=False)
    def __str__(self):
        return self.name










   

    
