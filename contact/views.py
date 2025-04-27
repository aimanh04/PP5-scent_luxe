from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Thanks for reaching out! We will get back to you soon.'
            )
            return redirect('contact_page')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
