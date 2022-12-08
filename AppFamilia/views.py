from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse
# Create your views here.

def mostrarFamiliar(request):
    f1=Familiar(nombre='Cecilia',parentesco='madre',nacimiento='1973-10-01')
    f1.save()
    f2=Familiar(nombre='Dario',parentesco='padre',nacimiento='1970-09-22')
    f2.save()
    f3=Familiar(nombre='Abril',parentesco='hermana',nacimiento='1998-01-14')
    f3.save()
    lista_familiares=[f1,f2,f3]
    return render(request,'AppFamilia/familia.html',{"lista_familiares":lista_familiares})


