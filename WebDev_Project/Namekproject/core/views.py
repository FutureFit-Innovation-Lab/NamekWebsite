

# Create your views here.
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Blog, Contact, Newsletter, Service
from .form import ContactForm, NewsletterForm
from .serializers import BlogSerializer, ContactSerializer, NewsletterSerializer, ServiceSerializer

# === TRADITIONAL DJANGO VIEWS === #
def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def services(request):
    return render(request, 'core/services.html')

def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'core/blog.html', {'blogs': blogs})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home or success page
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})

def subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect after subscription
    return redirect('home')  # Redirect if accessed directly

# === DJANGO REST FRAMEWORK VIEWSETS === #
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer