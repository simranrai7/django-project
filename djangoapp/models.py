from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    modified =models.DateTimeField  (auto_now=True) 
    image =models.ImageField(upload_to='post/',null=True)

    def __str__(self):
        return self.title
