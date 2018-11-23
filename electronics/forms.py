# This is our form
from django import forms
class ContactForm(forms.Form):    #form-module, ContactForm- is a subclass derived from From class
    contact_name = forms.CharField(label="Enter Your Name:", required=True)
    contact_email = forms.EmailField(label="Enter Your Email-id:", required=True)
    content = forms.CharField(label="Your Message : ", required=True, widget=forms.Textarea)
  