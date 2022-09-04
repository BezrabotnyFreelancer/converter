import requests
response = requests.get('https://api.exchangerate-api.com/v4/latest/USD').json()
currencies = response.get('rates')
print(currencies)
