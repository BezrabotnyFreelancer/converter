from secrets import choice
from django.forms import Form
from django import forms
import requests

response = requests.get('https://api.exchangerate-api.com/v4/latest/USD').json()
currencies = response.get('rates')

choices_curr = [(x, x) for x in currencies.keys()]

widgets = {
    'class': 'form-control',
    'placeholders': {
        'amount': 0,
        'from_curr': 'USD',
        'to_curr': 'RUB'
    }
}


class ConverterForm(Form):
    amount = forms.IntegerField(label='Amount', help_text='Input amount',
                                widget=forms.TextInput(attrs=({'class': widgets['class'],
                                                                  'placeholder': widgets['placeholders']['amount']})))
    
    from_curr = forms.ChoiceField(label='From currency',choices=choices_curr, help_text='Choose start currency',
                                  widget=forms.Select(attrs=({'class': widgets['class'],
                                                                   'placeholder': widgets['placeholders']['from_curr']})))
    
    to_curr = forms.ChoiceField(label='To currency', choices=choices_curr, help_text='Choose a final currency',
                                widget=forms.Select(attrs=({'class': widgets['class'],
                                                                  'placeholder': widgets['placeholders']['to_curr']})))
    