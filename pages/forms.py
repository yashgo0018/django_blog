from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=250, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your name'
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your email'
    }))
    subject = forms.CharField(max_length=250, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Subject'
    }))
    message = forms.CharField(label="Your Message", widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your message'
    }), required=True)
