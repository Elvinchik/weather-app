from django import forms


class WeatherForms(forms.Form):
    city = forms.CharField(max_length=65)