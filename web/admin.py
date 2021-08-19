from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Project, Comment


# Register the Admin classes for Book using the decorator
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('code','name','status','providers','budget','link','deadline','laravel')
    list_filter = ['status']
    inlines = [CommentInline]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'comment')
    list_filter = ['project', 'user']



# admin.site.register(User, UserAdmin)
