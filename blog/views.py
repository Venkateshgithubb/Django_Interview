from django.shortcuts import render
from django.views.generic import ListView
from .models import *

class PostListView(ListView):
    model = Post

print("hari")
# Create your views here.
