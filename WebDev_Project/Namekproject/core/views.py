

# Create your views here.
from django.shortcuts import render, redirect
from django.http import Http404  # Import Http404
from rest_framework import viewsets
from .models import Blog, Contact, Newsletter, Service
from .form import ContactForm, NewsletterForm
from .serializers import BlogSerializer, ContactSerializer, NewsletterSerializer, ServiceSerializer
from django.contrib import messages

# === TRADITIONAL DJANGO VIEWS === #
def home(request):
    return render(request, 'core/home.html')    #These views use Django’s built-in render() and redirect() functions to display HTML pages and handle form submissions.

def about(request):
    return render(request, 'core/about.html')

def services(request):
    return render(request, 'core/services.html')

# Blog List View (Shows all blogs)
def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')  # Fetch all blogs
    return render(request, 'core/blog.html', {'blogs': blogs})

# Blog Detail View (Shows one blog using slug)
def blog_detail(request, slug):
    try:
        blog = Blog.objects.get(slug=slug)  # Fetch blog by slug
    except Blog.DoesNotExist:
        raise Http404("Blog not found")  # Show error if blog doesn't exist
    return render(request, 'core/blog_detail.html', {'blog': blog})


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
    if request.method == "POST":
        email = request.POST.get("email")
        
        if Newsletter.objects.filter(email=email).exists():
            messages.warning(request, "You are already subscribed!")
        else:
            Newsletter.objects.create(email=email)
            messages.success(request, "Subscription successful!")

    return redirect("home")  # Redirect to home page after subscribing

# === DJANGO REST FRAMEWORK VIEWSETS === #
 #A ModelViewSet automatically provides list, retrieve, create, update, and delete actions for the model.
#This means you don’t need to write separate views for these actions.
class BlogViewSet(viewsets.ModelViewSet):        
    queryset = Blog.objects.all()  #Fetches all records from the Blog model.
    serializer_class = BlogSerializer   #Specifies how the data should be formatted in the API response.

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer