from django import forms
from django.forms import widgets
# from django.utils.translation import gettext_lazy as _

from .models import Contact, Enquiry


class ContactForm(forms.ModelForm):
    class Meta:

        model = Contact
        exclude = ["timestamp"]
        widgets = {
            "name": widgets.TextInput(
                attrs={"class": "required form-control", "placeholder": "Your Name"}
            ),
            "phone": widgets.TextInput(
                attrs={
                    "class": "required form-control",
                    "placeholder": "Your Phone Number",
                }
            ),
            "email": widgets.EmailInput(
                attrs={
                    "class": "required form-control",
                    "placeholder": "Your Email Address",
                }
            ),
            "adress": widgets.TextInput(
                attrs={"class": "required form-control", "placeholder": "Your Adress"}
            ),
            "service": widgets.Select(
                attrs={"class": "required form-control", "placeholder": "Service"},            ),
            "message": widgets.Textarea(
                attrs={"class": "required form-control", "placeholder": "Message"}
            ),
        }


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        exclude = ["timestamp",'service']
        widgets = {
            "full_name": widgets.TextInput(
                attrs={"class": "required form-control", "placeholder": "Full Name"}
            ),
            "phone_number": widgets.TextInput(
                attrs={
                    "class": "required form-control",
                    "placeholder": "Your Phone Number",
                }
            ),
            "client_adress": widgets.TextInput(
                attrs={"class": "required form-control", "placeholder": "Your Adress"}
            ),
            "description": widgets.Textarea(
                attrs={
                    "class": "required form-control",
                    "placeholder": "Enter Your message",
                }
            ),
        }
