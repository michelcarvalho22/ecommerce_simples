# coding=utf-8

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, CreateView
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import Promocao
from catalog import views

from .forms import ContactForm


User = get_user_model()

def index(request):
<<<<<<< HEAD
    return redirect('catalog:product_list')



def contact(request):
=======
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")
>>>>>>> 9a41ac0e2988172bbf5e17295857bc863053ce8a

    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True

    elif request.method == 'POST':
        messages.error(request, 'Formulário inválido')

    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)

def promocao(request, slug):
    promocao = Promocao
    context = {
        'promocao': promocao
    }
    return render(request, 'catalog/product.html', context)

<<<<<<< HEAD

=======
    return render(request, "db.html", {"greetings": greetings})
>>>>>>> 9a41ac0e2988172bbf5e17295857bc863053ce8a
