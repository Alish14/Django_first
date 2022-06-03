from django import forms
from blog.models import comment

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = comment
        fields = ['post','name','email','subject','message']
        
