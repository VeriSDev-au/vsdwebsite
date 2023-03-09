from django.contrib import admin

from .models import UserProfile
from app_blog.models import BlogPost

admin.site.register(UserProfile)
admin.site.register(BlogPost)
