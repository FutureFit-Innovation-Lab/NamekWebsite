from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BlogViewSet, ContactViewSet, NewsletterViewSet, ServiceViewSet,
    home, about, services, blog_list, contact, subscribe
)

# API Router for DRF ViewSets
router = DefaultRouter()
router.register(r'blogs', BlogViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'newsletters', NewsletterViewSet)
router.register(r'services', ServiceViewSet)

urlpatterns = [
    # Traditional Views
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('blog/', blog_list, name='blog'),  # Matches your template
    path('contact/', contact, name='contact'),
    path('subscribe/', subscribe, name='subscribe'),

    # API Endpoints
    path('api/', include(router.urls)),
]