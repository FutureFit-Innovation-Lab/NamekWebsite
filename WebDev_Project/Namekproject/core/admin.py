

# Register your models here.
from django.contrib import admin
from .models import Blog, Contact, Newsletter, Service

#admin.site.register(Blog) (these are the normal way to register your model but to improve i use the current one activ now)
#admin.site.register(Contact)
#admin.site.register(Newsletter)
#admin.site.register(Service)

# Blog Admin
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Removed 'author'
    search_fields = ('title', 'content')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    prepopulated_fields = {'slug': ('title',)}

# Contact Admin
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_at')  # Fixed 'name' → 'first_name' & 'last_name'
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('created_at',)

# Newsletter Admin
@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)

# Service Admin
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  # Fixed 'name' → 'title'
    search_fields = ('title',)