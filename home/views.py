from django.shortcuts import render
from django.http import HttpResponse
from post.models import Post
from django.views.generic.list import ListView
from django.http import JsonResponse
from django.forms.models import model_to_dict

import json

# def index(request):
#     posts = Post.objects.all()
#     context = {
#         'posts': posts,
#         'variable': 'I am a context variable'
#     }
#     return render(request, 'index.html', context)


class PostCollection(ListView):
    model = Post
    paginate_by = 9
    template_name="index.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        return context
