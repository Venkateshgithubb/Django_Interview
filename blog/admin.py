from django.contrib import admin
from .models import Post, PublishedPost, Category, AuthorProfile


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "author", "category", "created_at")
    list_filter = ("status", "category")
    search_fields = ("title", "body")

@admin.register(PublishedPost)
class PublishedPostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "created_at")