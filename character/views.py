from django.shortcuts import render
from .models import Character
from django.views import View
from django.views.generic.base import TemplateView
from django.shortcuts import redirect

from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .forms import CharacterUpdateForm

from django.http import JsonResponse 

import json
class CharSheetView(TemplateView):
    template_name = 'charsheet.html'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        char_id = self.kwargs['id']
        character = Character.objects.get(id=char_id)
        context_vars = {
            'character': character
        }
        context.update(context_vars)
        return context
    
class CharacterCreateView(LoginRequiredMixin, CreateView):
    template_name = 'character_form.html'
    model = Character
    fields = [
        'name',
        'char_class',
        'level',
        'description',
        'image',
    ]



class CharacterUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'character_update_form.html'
    model = Character
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
    #     char = Character.objects.get(id=char_id)
    #     form = CharacterUpdateForm(new_values, instance=char)
    #     if form.is_valid():
    #         form.save()
    #         return JsonResponse({
    #             'success': True,
    #             'message': 'Character sheet updated!'
    #         })
    #     return JsonResponse({
    #         'success': False,
    #         'message': 'Error in Form!'
    #     })