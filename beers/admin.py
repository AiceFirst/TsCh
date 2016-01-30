from django.contrib import admin
from .models import Post, BadWords

# Register your models here.
admin.site.register(Post)
admin.site.register(BadWords)
