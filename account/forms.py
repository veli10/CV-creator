from django import forms 
from .models import FormModel, ContactModel

class ResumeForm(forms.ModelForm):
    
    class Meta:
        model = FormModel
        fields = ["username","surname","age", "job", "university", "experience", "hobies", "languages"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'job': forms.TextInput(attrs={'class': 'form-control'}),
            'university': forms.TextInput(attrs={'class': 'form-control'}),
            'experience': forms.Textarea(attrs={'class': 'form-control'}),
            'hobies': forms.Textarea(attrs={'class': 'form-control'}),
            'languages': forms.Textarea(attrs={'class': 'form-control'}),
        }

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = ContactModel
        fields = ["username","surname","message"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }