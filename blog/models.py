from django.conf import settings
from django.db import models
from .managers import PublishedPostManager

class AuthorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

class Post(models.Model):
    STATUS_CHOICES = [("DRAFT", "Draft"), ("PUBLISHED", "Published")]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="posts")
    title = models.CharField(max_length=200)
    body = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="DRAFT")
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()                 # default
    published = PublishedPostManager()         # custom manager

class PublishedPost(Post):
    """
    Proxy model: no new table.
    Used for alternate behavior/admin, different default ordering, etc.
    """
    class Meta:
        proxy = True
        ordering = ["-created_at"]
  