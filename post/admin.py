from django.contrib import admin
from .models import Post



class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            'Info', {
                'fields': (
                    'title',
                    'image',
                    'body'

                )
            }
        ),
    )

# Register your models here.
admin.site.register(Post, PostAdmin)
