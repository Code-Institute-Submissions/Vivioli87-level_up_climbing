from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages

from .forms import ContactForm
from .models import GeneralContact

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully submitted enquiry!')
            return redirect('home')

    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def contact_manager(request):

    general_contacts = GeneralContact.objects.all().order_by('-date_sent')

    template = 'contact/contact_manager.html'

    context = {
        'general_contacts': general_contacts,
    }

    return render(request, template, context)