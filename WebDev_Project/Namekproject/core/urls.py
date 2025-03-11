from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BlogViewSet, ContactViewSet, NewsletterViewSet, ServiceViewSet,
    home, about, services, blog_list, blog_detail, contact, subscribe
)

# API Router for DRF ViewSets
router = DefaultRouter() #Creates a set of RESTful API routes automatically.
router.register(r'blogs', BlogViewSet)  #This maps URLs like /api/blogs/ to the BlogViewSet.
router.register(r'contacts', ContactViewSet)
router.register(r'newsletters', NewsletterViewSet)
router.register(r'services', ServiceViewSet)

urlpatterns = [
    # Traditional Views
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),

    # blog url
    path('blog/', blog_list, name='blog'),  # Matches your template
     path('blog/<slug:slug>/', blog_detail, name='blog_detail'),
    
    path('contact/', contact, name='contact'),
    path('subscribe/', subscribe, name='subscribe'),

    # API Endpoints
    path('api/', include(router.urls)),  #Includes all the auto-generated API routes in Django’s urlpatterns.
]



#When building APIs in Django REST Framework, ViewSets and Routers help manage
#  API endpoints efficiently. Instead of writing separate views for each operation
#  (like GET, POST, DELETE), ViewSets bundle these actions together. Routers automatically 
# create URL patterns for them.

#A ViewSet is a special type of Django view that handles CRUD operations 
# (Create, Read, Update, Delete) for a model automatically. 
# It reduces the need to write separate views for each action.