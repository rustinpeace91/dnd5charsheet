from django.shortcuts import render
from .models import Post
from django.views import View
from django.views.generic.base import TemplateView
from django.shortcuts import redirect

from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .forms import PostUpdateForm

from django.http import JsonResponse 

import json
class PostsheetView(TemplateView):
    template_name = 'postsheet.html'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        char_id = self.kwargs['id']
        post = Post.objects.get(id=char_id)
        context_vars = {
            'post': post
        }
        context.update(context_vars)
        return context
    
class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'post_form.html'
    model = Post
    fields = [
        'name',
        'char_class',
        'level',
        'description',
        'image',
    ]



class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'post_update_form.html'
    model = Post
    fields = [
        'name',
        'char_class',
        'level',
        'description',
        'image',
    ]
    # def post(self, request, **args):
    #     char_id = self.kwargs['id']
    #     new_values = json.loads(request.POST['form'])
    #     char = Post.objects.get(id=char_id)
    #     form = PostUpdateForm(new_values, instance=char)
    #     if form.is_valid():
    #         form.save()
    #         return JsonResponse({
    #             'success': True,
    #             'message': 'Post sheet updated!'
    #         })
    #     return JsonResponse({
    #         'success': False,
    #         'message': 'Error in Form!'
    #     })