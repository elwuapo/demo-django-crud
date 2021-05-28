from core.models import Perro, Raza
from django.shortcuts import redirect, render


def Inicio(request):
    contexto = {}
    return render(request, 'inicio.html', contexto)

def Perros(request):
    perros = Perro.objects.all()
    contexto = {'perros': perros}

    return render(request, 'perros.html', contexto)

def FormularioPerroAgr(request):
    razas = Raza.objects.all()
    contexto = {'razas': razas}

    return render(request, 'agr_perro.html', contexto)

def FormularioPerroMod(request, nro_chip):
    perro = Perro.objects.get(nro_chip=nro_chip)
    razas = Raza.objects.all()
    contexto = {'razas': razas, 'perro': perro}

    return render(request, 'mod_perro.html', contexto)

def AgregarPerro(request):
    id_raza = request.POST.get('raza', '')
    raza = Raza.objects.get(id = id_raza)
    
    nro_chip = request.POST.get('nro_chip', '')
    nombre = request.POST.get('nombre', '')
    imagen = request.FILES.get('imagen', '')

    perro = Perro(nro_chip=nro_chip, nombre=nombre, raza=raza, imagen=imagen)
    perro.save()

    return redirect('Perros')

def ModificarPerro(request):
    id_raza = request.POST.get('raza', '')
    raza = Raza.objects.get(id = id_raza)
    
    nro_chip = request.POST.get('nro_chip', '')
    nombre = request.POST.get('nombre', '')
    imagen = request.FILES.get('imagen', '')

    perro = Perro.objects.get(nro_chip=nro_chip)
    perro.nombre = nombre
    perro.raza = raza

    print(imagen)

    if(imagen != ''):
        perro.imagen = imagen
        
    perro.save()

    return redirect('Perros')

def EliminarPerro(request, nro_chip):
    perro = Perro.objects.get(nro_chip=nro_chip)
    perro.delete()

    return redirect('Perros')
