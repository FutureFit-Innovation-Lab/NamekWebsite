

# Create your models here.
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from datetime import datetime

# BLOG MODEL
class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)
    content = models.TextField()
    excerpt = models.TextField(null=True, blank=True)  # Add excerpt field
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    thumbnail = models.ImageField(upload_to='blog_thumbnails/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Automatically generate slug from title if not provided
            self.slug = slugify(self.title)
        
        
        if not self.excerpt:  # Automatically generate excerpt if not provided
            self.excerpt = self.content[:300] + '...' if len(self.content) > 300 else self.content

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})   # Returns the dynamic URL for this blog post

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']   # Order blogs by most recent first

# CONTACT MODEL
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
# NEWSLETTER MODEL
class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
# SERVICE MODEL
class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=100)  # Store Bootstrap icon class
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
    # VISITOR MODEL to track visitor information.
class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip_address

    @classmethod
    def monthly_visits(cls):
        return cls.objects.extra(select={'month': "strftime('%%m', timestamp)"}).values('month').annotate(count=models.Count('id')).order_by('month')

    @classmethod
    def month_with_highest_visits(cls):    #Finds the month with the highest visits.

        result = cls.monthly_visits().order_by('-count').first()
        return result['month'] if result else 'No visits yet'