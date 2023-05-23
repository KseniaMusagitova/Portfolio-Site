from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'date_posted', 'date_updated', 'status',]
    list_filter = ['status', 'date_posted', 'date_updated']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date_posted'
    ordering = ['status', 'date_posted']
