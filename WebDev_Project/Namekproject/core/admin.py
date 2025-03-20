

# Register your models here.
from django.contrib import admin
from .models import Blog, Contact, Newsletter, Service, Visitor

#admin.site.register(Blog) (these are the normal way to register your model but to improve it in the django admin dashbord, i decided to use the current one active now)
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

# Visitor Admin
@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'timestamp', 'get_month', 'get_year')    #list_display shows visitor details.
    search_fields = ('ip_address',)
    list_filter = ('timestamp',)

    def get_month(self, obj):
        return obj.timestamp.strftime('%B')  # Month name
    get_month.short_description = 'Month'

    def get_year(self, obj):
        return obj.timestamp.year
    get_year.short_description = 'Year'

    def changelist_view(self, request, extra_context=None):          #changelist_view adds monthly statistics to the admin page.
        search_fields = ('ip_address',)
        extra_context = extra_context or {}
        extra_context['monthly_visits'] = Visitor.monthly_visits()
        extra_context['peak_month'] = Visitor.month_with_highest_visits()
        return super().changelist_view(request, extra_context=extra_context)