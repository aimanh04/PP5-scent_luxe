from django.shortcuts import render, redirect
from .models import ContactMessage
from django.contrib import messages

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, "Thank you for contacting us!")
            return redirect('contact')
        else:
            messages.error(request, "Please fill out all fields.")

    return render(request, 'contact/contact.html')