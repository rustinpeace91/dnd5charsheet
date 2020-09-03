from .models import Post
from django.forms import ModelForm 
from django.core.exceptions import ValidationError
class PostUpdateForm(ModelForm):

    def clean(self):
        cleaned_data = super().clean()


    class Meta:
        model = Post
        fields = (
            'title',
            'body', 
            'image'
        )