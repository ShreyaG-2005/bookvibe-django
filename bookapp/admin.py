from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


# Customize the user admin form
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'is_staff', 'date_joined')  # fields to display in list
    search_fields = ('username', 'email')  # Add search functionality
    list_filter = ('is_staff', 'is_active')  # Add filter functionality

# Register the custom user admin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
from django.contrib import admin
from .models import Book, UserBookStatus
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status')

# Register Book model
admin.site.register(Book)

# Register UserBookStatus model
admin.site.register(UserBookStatus)
