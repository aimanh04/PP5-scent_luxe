from django.shortcuts import render
from .models import FAQ

def faq(request):
    questions = FAQ.objects.all()
    return render(request, 'faq/faq.html', {'questions': questions})