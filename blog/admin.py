from django.contrib import admin
from .models import Note, Category, Task


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'priority', 'is_pinned', 'category', 'updated_at')
    list_filter = ('priority', 'is_pinned', 'category')
    search_fields = ('title', 'content')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')
    search_fields = ('name',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'note', 'owner', 'is_done')
    list_filter = ('is_done',)
    search_fields = ('title',)
