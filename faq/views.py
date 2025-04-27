from django.shortcuts import render
from .models import FAQ


def faq(request):
    candles = FAQ.objects.filter(category='candles')
    shipping = FAQ.objects.filter(category='shipping')
    return render(request, 'faq/faq.html', {
        'candles': candles,
        'shipping': shipping,
    })