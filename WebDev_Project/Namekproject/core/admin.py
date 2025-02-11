

# Register your models here.
from django.contrib import admin
from .models import Blog, Contact, Newsletter, Service

admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(Newsletter)
admin.site.register(Service)