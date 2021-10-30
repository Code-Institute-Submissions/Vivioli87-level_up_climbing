from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .forms import ContactForm, CompleteContactForm, PrivateCoachingForm, CompletePrivateCoachingForm
from .models import GeneralContact, PrivateCoachingContact


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully submitted enquiry!')
            return redirect('home')
        else:
            messages.error(request,
                           ('Failed to submit enquiry. '
                            'Please ensure the form is valid.'))

    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def coaching_contact_form(request):
    if request.method == 'POST':
        form = PrivateCoachingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully submitted 1:1 coaching enquiry!')
            return redirect('home')
        else:
            messages.error(request,
                           ('Failed to submit enquiry. '
                            'Please ensure the form is valid.'))

    else:
        form = PrivateCoachingForm()

    template = 'contact/coaching_contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def contact_manager(request):

    general_contacts = GeneralContact.objects.filter(is_complete=False).order_by('-date_sent')
    coaching_contacts = PrivateCoachingContact.objects.filter(is_complete=False).order_by('-date_sent')
    
    template = 'contact/contact_manager.html'

    context = {
        'general_contacts': general_contacts,
        'coaching_contacts': coaching_contacts,
    }

    return render(request, template, context)


def contact_detail(request, contact_id):
    contact = get_object_or_404(GeneralContact, pk=contact_id)

    if request.method == 'POST':
        form = CompleteContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully completed enquiry!')
            return redirect(reverse('contact_manager'))
        else:
            messages.error(request,
                           ('Failed to mark enquiry as complete. '
                            'Please ensure the form is valid.'))

    else:
        form = CompleteContactForm(instance=contact)

    template = 'contact/contact_detail.html'

    context = {
        'form': form,
        'contact': contact,
    }

    return render(request, template, context)


def coaching_contact_detail(request, contact_id):
    contact = get_object_or_404(PrivateCoachingContact, pk=contact_id)

    if request.method == 'POST':
        form = CompletePrivateCoachingForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully completed coaching enquiry!')
            return redirect(reverse('contact_manager'))
        else:
            messages.error(request,
                           ('Failed to mark enquiry as complete. '
                            'Please ensure the form is valid.'))

    else:
        form = CompletePrivateCoachingForm(instance=contact)

    template = 'contact/coaching_contact_detail.html'

    context = {
        'form': form,
        'contact': contact,
    }

    return render(request, template, context)
