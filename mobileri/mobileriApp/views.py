from django.shortcuts import render, redirect, get_object_or_404 
from .models import *

# Create your views here.

def home(request):
    produktet_e_fundit = Produkti.objects.filter(eshte_aktiv=True).order_by('-data_krijimit')[:3]
    return render(request, "home.html", {'produktet_e_fundit': produktet_e_fundit})

def navbar(request):
    return render(request,"navbar.html")

def base(request):
    return render(request,"base.html")



def produktet(request):
    produktet = Produkti.objects.filter(eshte_aktiv=True).order_by('-data_krijimit')
    kategorite = Kategoria.objects.all()
    
    context = {
        'produktet': produktet,
        'kategorite': kategorite,
    }
    return render(request, 'produktet.html', context)

def detajet(request, pk):
    produkti = get_object_or_404(Produkti, pk=pk, eshte_aktiv=True)
    return render(request, 'detajet.html', {'produkti': produkti})


