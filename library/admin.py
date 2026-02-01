from django.contrib import admin
from .models import LibraryBook

@admin.register(LibraryBook)
class LibraryBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'available')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('available',)
