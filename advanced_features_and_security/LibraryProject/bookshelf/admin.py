from django.contrib import admin
from .models import Book,CustomUser
from django.contrib.auth.admin import UserAdmin

# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'publication_year','username','email','date_of_birth','is_staff')
#     list_filter = ('title', 'author', 'publication_year')
#     search_fields = ('title', 'author', 'publication_year')

# admin.site.register(Book,BookAdmin)

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')})
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')})
    )
    
    list_display = ('email', 'is_staff', 'date_of_birth', 'username')

admin.site.register(CustomUser , CustomUserAdmin)