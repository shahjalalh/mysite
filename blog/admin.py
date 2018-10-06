from django.contrib import admin
from blog.models import Post, Comment

# Register your models here.
admin.site.resister(Post)
admin.site.resister(Comment)
