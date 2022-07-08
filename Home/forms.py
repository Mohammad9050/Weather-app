from django import forms


class get_city(forms.Form):
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'container'}))
