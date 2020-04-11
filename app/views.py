from django.shortcuts import render, redirect
from .forms import ReservaForm


# Create your views here.

from .models import *

def mostrar_inicio(request):
    return render(request, 'home.html')
    
def mostrar_departamentos(request):
    departamentos = Departamento.objects.all()
    context = {'departamentos': departamentos}
    return render(request, 'departamentos.html', context)


def mostrar_seleccionado(request, pk):
        departamento_seleccionado = Departamento.objects.get(pk=pk)
        form = ReservaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.departamento = departamento_seleccionado
            post.save()
        reservas = Reserva.objects.filter(departamento = departamento_seleccionado)
        return render(request, 'seleccionado.html', {'departamento_seleccionado': departamento_seleccionado, 'reservas':reservas, 'form':form})
