from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def home_view(request):
    return render(request, 'reseña.html')

def create_relacion(request):
    if request.method == 'POST':
        relacion = request.POST['relacion']
        TblRelacioncomercial.objects.create(relacion=relacion)
        return redirect('list_relaciones')

    return render(request, 'relacion.html')

def list_relaciones(request):
    relaciones = TblRelacioncomercial.objects.all()
    return render(request, 'relacion.html', {'relaciones': relaciones})

def edit_relacion(request, relacion_id):
    relacion = get_object_or_404(TblRelacioncomercial, id=relacion_id)

    if request.method == 'POST':
        relacion.relacion = request.POST['relacion']
        relacion.save()
        return redirect('list_relaciones')

    return render(request, 'edit_relacion.html', {'relacion': relacion})

def delete_relacion(request):
    if request.method == 'POST':
        relacion_id = request.POST['relacion_id']
        relacion = get_object_or_404(TblRelacioncomercial, id=relacion_id)
        relacion.delete()
        return redirect('list_relaciones')

    return redirect('list_relaciones')


def create_organizacion(request):
    if request.method == 'POST':
        denominacion = request.POST['denominacion']
        ruc = request.POST['ruc']
        direccion = request.POST['direccion']
        departamento = request.POST['departamento']
        provincia = request.POST['provincia']
        distrito = request.POST['distrito']
        notas = request.POST['notas']
        relacion_id = request.POST['relacion']  # Obtener el ID de la relación seleccionada

        # Buscar la relación comercial seleccionada en la base de datos
        relacion = get_object_or_404(TblRelacioncomercial, id=relacion_id)

        TblOrganizacion.objects.create(
            denominacion=denominacion,
            ruc=ruc,
            direccion=direccion,
            departamento=departamento,
            provincia=provincia,
            distrito=distrito,
            notas=notas,
            id_relacion=relacion  # Asignar la relación comercial a la organización
        )
        return redirect('list_organizaciones')

    else:
        # Si la solicitud es GET, obtener todas las relaciones para mostrarlas en el desplegable
        relaciones = TblRelacioncomercial.objects.all()
        return render(request, 'crear_organizacion.html', {'relaciones': relaciones})

def list_organizaciones(request):
    organizaciones = TblOrganizacion.objects.all()
    return render(request, 'organizacion.html', {'organizaciones': organizaciones})

def edit_organizacion(request, organizacion_id):
    organizacion = get_object_or_404(TblOrganizacion, id=organizacion_id)

    if request.method == 'POST':
        # Obtener todas las relaciones para mostrarlas en el desplegable
        relaciones = TblRelacioncomercial.objects.all()

        organizacion.denominacion = request.POST['denominacion']
        organizacion.ruc = request.POST['ruc']
        organizacion.direccion = request.POST['direccion']
        organizacion.departamento = request.POST['departamento']
        organizacion.provincia = request.POST['provincia']
        organizacion.distrito = request.POST['distrito']
        organizacion.notas = request.POST['notas']
        organizacion.save()
        return redirect('list_organizaciones')

    else:
        # Si la solicitud es GET, obtener todas las relaciones para mostrarlas en el desplegable
        relaciones = TblRelacioncomercial.objects.all()
        return render(request, 'edit_organizacion.html', {'organizacion': organizacion, 'relaciones': relaciones})

def delete_organizacion(request):
    if request.method == 'POST':
        organizacion_id = request.POST['organizacion_id']
        organizacion = get_object_or_404(TblOrganizacion, id=organizacion_id)
        organizacion.delete()
        return redirect('list_organizaciones')

    return redirect('list_organizaciones')


