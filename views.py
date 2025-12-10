from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Project, Client
from .forms import ContactForm, SubscriberForm

def index(request):
    projects = Project.objects.all()
    clients = Client.objects.all()

    contact_form = ContactForm()
    subscriber_form = SubscriberForm()

    if request.method == "POST":
        if 'contact_submit' in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                return redirect('/')
        elif 'subscribe_submit' in request.POST:
            subscriber_form = SubscriberForm(request.POST)
            if subscriber_form.is_valid():
                subscriber_form.save()
                return redirect('/')

    return render(request, 'index.html', {
        'projects': projects,
        'clients': clients,
        'contact_form': contact_form,
        'subscriber_form': subscriber_form
    })
