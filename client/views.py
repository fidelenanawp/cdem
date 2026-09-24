from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from client.models import Client
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
# Create your views here.

User=get_user_model()


def home(request):
    return render(request, 'client/home.html')


def check_code(request,qrcode):

    if request.user.is_authenticated:
        try:
            client=Client.objects.get(qrcode=qrcode)
            context = {'client':client}
            return render(request, 'client/check.html', context)
        except Client.DoesNotExist:
            context = {'client':None}
            return redirect('norecord')
    return redirect('home')

def details(request,pk):

    if request.user.is_authenticated:
        try:
            client=Client.objects.get(pk=pk)
            context = {'client':client}
            return render(request, 'client/details.html', context)
        except Client.DoesNotExist:
            context = {'client':None}
            return redirect('list')
    return redirect('home')


def list(request,event_location):
    if request.user.is_authenticated:
        clients=Client.objects.filter(event_location=event_location).order_by('first_name','last_name')
        context = {'clients':clients,
                   'event_location':event_location
        }
        return render(request, 'client/list.html', context)
    return redirect('home')



def norecord(request):
    return render(request, 'client/norecord.html')


@login_required
@require_POST

def client_validate(request, pk):
    """Valide le dossier du client (action du bouton « Confirmer et valider »)."""
    client = get_object_or_404(Client, pk=pk)

    if client.validated:
        messages.info(request, "Ce dossier a déjà été validé.")
    else:
        client.validated = True
        client.validation_datetime = timezone.now()
        client.valided_by = request.user.get_username()
        client.save(update_fields=["validated", "validation_datetime", "valided_by"])
        messages.success(request, "Le dossier a été validé avec succès.")

    return redirect("check", qrcode=client.qrcode)
