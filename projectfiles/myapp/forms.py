from django import forms
class Userinfoform(forms.Form):
    name= forms.CharField(label='your Name',max_length=10)
    email = forms.EmailField(label='your Email')
    message=forms.CharField(max_length=100)
