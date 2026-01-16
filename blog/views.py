from django.shortcuts import render
from django.views.generic import ListView
from .models import *

class PostListView(ListView):
    model = Post

# Create your views here.
