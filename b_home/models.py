from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_summernote.fields import SummernoteTextField

STATUS = ((0, "Draft"), (1, "Approved"))

class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    content = SummernoteTextField()
    image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
