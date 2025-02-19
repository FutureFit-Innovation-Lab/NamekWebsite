from rest_framework import serializers
from .models import Blog, Contact, Newsletter, Service #importing the models to be serialized

class BlogSerializer(serializers.ModelSerializer): #converts Blog model instances into JSON format.
    class Meta:
        model = Blog
        fields = '__all__'  # Serialize all fields

class ContactSerializer(serializers.ModelSerializer):     #Used to convert Contact model instances into JSON.
    class Meta:
        model = Contact                                     #This allows API users to retrieve or submit contact form data
        fields = '__all__'

class NewsletterSerializer(serializers.ModelSerializer):      #Converts Newsletter model data into JSON.
    class Meta:                                                 #This is useful for managing newsletter subscriptions via API.
        model = Newsletter
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):               #Converts Service model instances into JSON.                                        
    class Meta:                                         #This makes it possible to display services on a frontend application via API.
        model = Service
        fields = '__all__'