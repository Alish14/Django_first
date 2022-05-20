from django import forms
from website.models import Contact,Newsletter
class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'
        

class Newsletterform(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'
