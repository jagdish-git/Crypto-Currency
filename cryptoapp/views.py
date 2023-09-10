from django.shortcuts import render
import requests
import json


def home_fun(request):
    # get price of crypto currency
    price_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD,EUR')
    price = json.loads(price_request.content)

    # get news of crypto currency
    api_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api = json.loads(api_request.content)

    return render(request, 'home.html', {'api': api, 'price': price})

def prices(request):
    if request.method == "POST":
        quote = request.POST['quote']
        crypto_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms='+ quote +'&tsyms=USD')
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote': quote, 'crypto':crypto})
    else:
        notfound = 'Get the crypto on the above search bar...^_^'
        return render(request, 'prices.html', {'notfound': notfound})
