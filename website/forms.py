from django import forms
from website.models import Contact,Newsletter
from captcha.fields import CaptchaField
from django.forms import Textarea


class ContactForm(forms.ModelForm):    
    captcha = CaptchaField(label="")

    class Meta:
        model = Contact
        fields = '__all__'
        

class Newsletterform(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'

