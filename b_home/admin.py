from django.contrib import admin
from .models import Post, Category
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    
    list_display = ('title', 'slug', 'created_on', 'updated_on', 'status')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'slug')
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}