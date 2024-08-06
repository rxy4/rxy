from django.contrib import admin

# Register your models here.
from .models import Blog,BlogComment,BlogCategory


class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','content','pub_time','category','author']

class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['content','pub_time','author','blog']


admin.site.register(BlogCategory,BlogCategoryAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(BlogComment,BlogCommentAdmin)