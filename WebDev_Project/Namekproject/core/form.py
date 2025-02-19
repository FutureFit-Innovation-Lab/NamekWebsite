from django import forms
from .models import Contact, Newsletter

class ContactForm(forms.ModelForm):   #Creates a form based on the Contact model using ModelForm.
    class Meta:      #Meta class defines which model (Contact) and which fields will be included in the form.
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'message']

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']  #Creates a form to collect newsletter subscriptions (only requires an email).

        #Django automatically generates a form with first_name, last_name, email, and message fields using the contact as an example
        #When a user submits the form, Django checks if all fields are correctly filled before saving the data.
