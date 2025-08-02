from django.contrib import admin
from .models import Book,CreateUser

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year','username','email','date_of_birth','is_staff')
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')

admin.site.register(Book)


