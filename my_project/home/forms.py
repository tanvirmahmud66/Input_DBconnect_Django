from django import forms

class ContactInput(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(initial="email@email.com")
    password = forms.CharField()
    contact = forms.CharField(initial="+880")