from django.db import models

# Create your models here
class BlogPost(models.Model):
    title =models.CharField(max_length=200)
    content=models.TextField()
    author=models.CharField(max_length=30)
    email=models.EmailField(null=True,blank=True)
    phone=models.CharField(null=True,blank=True,max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
