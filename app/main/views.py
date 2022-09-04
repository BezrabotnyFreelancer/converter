from django.shortcuts import render
from .forms import ConverterForm, widgets, currencies
import requests

def main(request):
    if request.method == 'POST':
        convert_form = ConverterForm(request.POST)
        
        if convert_form.is_valid():
            
            amount = float(convert_form.cleaned_data['amount'])
            from_curr = convert_form.cleaned_data['from_curr']
            to_curr = convert_form.cleaned_data['to_curr']
            
            widgets['placeholders']['amount'] = amount
            widgets['placeholders']['from_curr'] = from_curr
            widgets['placeholders']['to_curr'] = to_curr
                 
            res = round((currencies[to_curr] / currencies[from_curr] * amount), 2)
            
            context = {
                'form': convert_form,
                'res': res
            }
            
            return render(request, 'main/index.html', context)
        
    else:
                
        convert_form = ConverterForm()
        context = {'form': convert_form}
        return render(request, 'main/index.html', context)
