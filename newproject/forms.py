from django import forms

class CarForm(forms.Form):
    name = forms.CharField( max_length=255)
    price = forms.DecimalField()
    images =forms.Textarea()
    characteristic =forms.Textarea()
    