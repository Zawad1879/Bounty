from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=False, max_length=100)
    email = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea)
