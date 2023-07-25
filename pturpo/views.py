from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.contrib import messages
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

        # Verificar si hay registros asociados en el otro modelo usando la ForeignKey 'id_relacion'
        if TblOrganizacion.objects.filter(id_relacion=relacion).exists():
            messages.error(request, 'No puedes eliminar esta relación comercial porque está siendo utilizada en otras organizaciones.')
        else:
            relacion.delete()
            messages.success(request, 'La relación comercial ha sido eliminada exitosamente.')
    
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

        # Obtener el ID de la relación comercial seleccionada del formulario
        id_relacion_comercial = request.POST.get('relacion', None)

        # Si se seleccionó una relación comercial válida, actualizamos el campo correspondiente de la organización
        if id_relacion_comercial:
            organizacion.id_relacion_id = id_relacion_comercial

        # Resto de los campos de la organización
        organizacion.denominacion = request.POST['denominacion']
        organizacion.ruc = request.POST['ruc']
        organizacion.direccion = request.POST['direccion']
        organizacion.departamento = request.POST['departamento']
        organizacion.provincia = request.POST['provincia']
        organizacion.distrito = request.POST['distrito']
        organizacion.notas = request.POST['notas']

        # Guardamos los cambios
        organizacion.save()

        return redirect('list_organizaciones')

    else:
        # Si la solicitud es GET, obtener todas las relaciones para mostrarlas en el desplegable
        relaciones = TblRelacioncomercial.objects.all()
        return render(request, 'edit_organizacion.html', {'organizacion': organizacion, 'relaciones': relaciones})
def delete_organizacion(request):
    if request.method == 'POST':
        organizacion_id = request.POST.get('organizacion_id')
        organizacion = get_object_or_404(TblOrganizacion, id=organizacion_id)

        # Verificar si hay registros asociados en el otro modelo usando la ForeignKey 'id_organizacion'
        if TblProyecto.objects.filter(id_organizacion=organizacion).exists():
            messages.error(request, 'No puedes eliminar esta organización porque está siendo utilizada en otros proyectos.')
        else:
            organizacion.delete()
            messages.success(request, 'La organización ha sido eliminada exitosamente.')

        return redirect('list_organizaciones')

def create_contacto(request):
    if request.method == 'POST':
        nom_contacto = request.POST['nom_contacto']
        apell_contacto = request.POST['apell_contacto']
        cargo = request.POST['cargo']
        correo = request.POST['correo']
        telefono = request.POST['telefono']
        celular = request.POST['celular']
        notas = request.POST['notas']
        relacion_id = request.POST['relacion']  # Obtener el ID de la relación seleccionada

        # Buscar la organización relacionada seleccionada en la base de datos
        organizacion = get_object_or_404(TblOrganizacion, id=relacion_id)

        TblContacto.objects.create(
            id_relacion=organizacion,
            nom_contacto=nom_contacto,
            apell_contacto=apell_contacto,
            cargo=cargo,
            correo=correo,
            telefono=telefono,
            celular=celular,
            notas=notas
        )
        return redirect('list_contactos')

    else:
        # Si la solicitud es GET, obtener todas las organizaciones para mostrarlas en el desplegable
        organizaciones = TblOrganizacion.objects.all()
        return render(request, 'crear_contacto.html', {'organizaciones': organizaciones})
def list_contactos(request):
    contactos = TblContacto.objects.all()
    return render(request, 'contacto.html', {'contactos': contactos})
def edit_contacto(request, contacto_id):
    contacto = get_object_or_404(TblContacto, id=contacto_id)

    if request.method == 'POST':
        # Obtener todas las organizaciones para mostrarlas en el desplegable
        organizaciones = TblOrganizacion.objects.all()

        # Obtener el ID de la organización seleccionada del formulario
        id_organizacion = request.POST.get('organizacion', None)

        # Si se seleccionó una organización válida, actualizamos el campo correspondiente del contacto
        if id_organizacion:
            organizacion = get_object_or_404(TblOrganizacion, id=id_organizacion)
            contacto.id_relacion = organizacion

        # Resto de los campos del contacto
        contacto.nom_contacto = request.POST['nom_contacto']
        contacto.apell_contacto = request.POST['apell_contacto']
        contacto.cargo = request.POST['cargo']
        contacto.correo = request.POST['correo']
        contacto.telefono = request.POST['telefono']
        contacto.celular = request.POST['celular']
        contacto.notas = request.POST['notas']

        # Guardamos los cambios
        contacto.save()

        return redirect('list_contactos')

    else:
        # Si la solicitud es GET, obtener todas las organizaciones para mostrarlas en el desplegable
        organizaciones = TblOrganizacion.objects.all()
        return render(request, 'edit_contacto.html', {'contacto': contacto, 'organizaciones': organizaciones})
def delete_contacto(request):
    if request.method == 'POST':
        contacto_id = request.POST.get('contacto_id')
        contacto = get_object_or_404(TblContacto, id=contacto_id)
        contacto.delete()
        return redirect('list_contactos')

    return redirect('list_contactos')

def create_categoria(request):
    if request.method == 'POST':
        categoria = request.POST['categoria']
        TblCategoriaP.objects.create(categoria=categoria)
        return redirect('list_categorias')

    return render(request, 'categoria.html')
def list_categorias(request):
    categorias = TblCategoriaP.objects.all()
    return render(request, 'categoria.html', {'categorias': categorias})
def edit_categoria(request, categoria_id):
    categoria = get_object_or_404(TblCategoriaP, id=categoria_id)

    if request.method == 'POST':
        categoria.categoria = request.POST['categoria']
        categoria.save()
        return redirect('list_categorias')

    return render(request, 'edit_categoria.html', {'categoria': categoria})
def delete_categoria(request):
    if request.method == 'POST':
        categoria_id = request.POST['categoria_id']
        categoria = get_object_or_404(TblCategoriaP, id=categoria_id)
        categoria.delete()
        return redirect('list_categorias')

    return redirect('list_categorias')

def create_proyecto(request):
    if request.method == 'POST':
        id_organizacion = request.POST['id_organizacion']
        id_categoria = request.POST['id_categoria']
        nom_proyecto = request.POST['nom_proyecto']
        prioridad = request.POST['prioridad']
        f_registro = request.POST['f_registro']
        f_inicio_p = request.POST['f_inicio_p']
        f_final_p = request.POST['f_final_p']
        presupuesto_p_t = request.POST['presupuesto_p_t']
        num_presupuesto_doc = request.POST['num_presupuesto_doc']
        observaciones = request.POST['observaciones']
        estado = request.POST['estado']

        # Buscar la organización y categoría correspondiente en la base de datos
        organizacion = get_object_or_404(TblOrganizacion, id=id_organizacion)
        categoria = get_object_or_404(TblCategoriaP, id=id_categoria)

        TblProyecto.objects.create(
            id_organizacion=organizacion,
            id_categoria=categoria,
            nom_proyecto=nom_proyecto,
            prioridad=prioridad,
            f_registro=f_registro,
            f_inicio_p=f_inicio_p,
            f_final_p=f_final_p,
            presupuesto_p_t=presupuesto_p_t,
            num_presupuesto_doc=num_presupuesto_doc,
            observaciones=observaciones,
            estado=estado
        )
        return redirect('list_proyectos')

    else:
        # Si la solicitud es GET, obtener todas las organizaciones y categorías para mostrarlas en los desplegables
        organizaciones = TblOrganizacion.objects.all()
        categorias = TblCategoriaP.objects.all()
        return render(request, 'crear_proyecto.html', {'organizaciones': organizaciones, 'categorias': categorias})
def list_proyectos(request):
    proyectos = TblProyecto.objects.all()
    return render(request, 'proyecto.html', {'proyectos': proyectos})
def edit_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(TblProyecto, id=proyecto_id)

    if request.method == 'POST':
        # Obtener todas las organizaciones y categorías para mostrarlas en los desplegables
        organizaciones = TblOrganizacion.objects.all()
        categorias = TblCategoriaP.objects.all()

        # Obtener el ID de la organización y categoría seleccionada del formulario
        id_organizacion = request.POST.get('id_organizacion', None)
        id_categoria = request.POST.get('id_categoria', None)

        # Si se seleccionó una organización y categoría válida, actualizamos los campos correspondientes del proyecto
        if id_organizacion and id_categoria:
            proyecto.id_organizacion_id = id_organizacion
            proyecto.id_categoria_id = id_categoria

        # Resto de los campos del proyecto
        proyecto.nom_proyecto = request.POST['nom_proyecto']
        proyecto.prioridad = request.POST['prioridad']

        # Verificar si los campos de fecha están vacíos antes de intentar asignarlos
        if request.POST['f_registro']:
            proyecto.f_registro = request.POST['f_registro']
        if request.POST['f_inicio_p']:
            proyecto.f_inicio_p = request.POST['f_inicio_p']
        if request.POST['f_final_p']:
            proyecto.f_final_p = request.POST['f_final_p']

        proyecto.presupuesto_p_t = request.POST['presupuesto_p_t']
        proyecto.num_presupuesto_doc = request.POST['num_presupuesto_doc']
        proyecto.observaciones = request.POST['observaciones']
        proyecto.estado = request.POST['estado']

        # Guardamos los cambios
        proyecto.save()

        return redirect('list_proyectos')

    else:
        # Si la solicitud es GET, obtener todas las organizaciones y categorías para mostrarlas en los desplegables
        organizaciones = TblOrganizacion.objects.all()
        categorias = TblCategoriaP.objects.all()
        return render(request, 'edit_proyecto.html', {'proyecto': proyecto, 'organizaciones': organizaciones, 'categorias': categorias})
def delete_proyecto(request):
    if request.method == 'POST':
        proyecto_id = request.POST.get('proyecto_id')
        proyecto = get_object_or_404(TblProyecto, id=proyecto_id)
        proyecto.delete()
        return redirect('list_proyectos')

    return redirect('list_proyectos')

def create_tarea(request):
    if request.method == 'POST':
        id_proyecto = request.POST['id_proyecto']
        nom_tarea = request.POST['nom_tarea']
        f_inicio_t = request.POST['f_inicio_t']
        f_final_t = request.POST['f_final_t']
        dias = request.POST['dias']
        presupuesto_t = request.POST['presupuesto_t']
        notas = request.POST['notas']
        estado = request.POST['estado']

        # Buscar el proyecto correspondiente en la base de datos
        proyecto = get_object_or_404(TblProyecto, id=id_proyecto)

        TblTarea.objects.create(
            id_proyecto=proyecto,
            nom_tarea=nom_tarea,
            f_inicio_t=f_inicio_t,
            f_final_t=f_final_t,
            dias=dias,
            presupuesto_t=presupuesto_t,
            notas=notas,
            estado=estado
        )
        return redirect('list_tareas')

    else:
        # Si la solicitud es GET, obtener todos los proyectos para mostrarlos en el desplegable
        proyectos = TblProyecto.objects.all()
        return render(request, 'crear_tarea.html', {'proyectos': proyectos})
def list_tareas(request):
    tareas = TblTarea.objects.all()
    return render(request, 'tarea.html', {'tareas': tareas})
def edit_tarea(request, tarea_id):
    tarea = get_object_or_404(TblTarea, id=tarea_id)
    proyectos = TblProyecto.objects.all()

    if request.method == 'POST':
        # Obtener los datos ingresados en el formulario
        id_proyecto = request.POST['id_proyecto']
        nombre_tarea = request.POST['nom_tarea']
        f_inicio_t = request.POST['f_inicio_t']
        f_final_t = request.POST['f_final_t']
        dias = request.POST['dias']
        presupuesto_t = request.POST['presupuesto_t']
        notas = request.POST['notas']
        estado = request.POST['estado']

        # Buscar el proyecto correspondiente en la base de datos
        proyecto = get_object_or_404(TblProyecto, id=id_proyecto)

        # Actualizar los atributos de la tarea con los nuevos valores
        tarea.id_proyecto = proyecto
        tarea.nom_tarea = nombre_tarea
        tarea.f_inicio_t = f_inicio_t
        tarea.f_final_t = f_final_t
        tarea.dias = dias
        tarea.presupuesto_t = presupuesto_t
        tarea.notas = notas
        tarea.estado = estado

        # Guardar los cambios en la tarea
        tarea.save()

        return redirect('list_tareas')

    # Si la solicitud es GET, mostrar el formulario con los datos de la tarea para su edición
    return render(request, 'edit_tarea.html', {'tarea': tarea, 'proyectos': proyectos})
def delete_tarea(request):
    if request.method == 'POST':
        tarea_id = request.POST.get('tarea_id')
        tarea = get_object_or_404(TblTarea, id=tarea_id)
        tarea.delete()
        return redirect('list_tareas')

    return redirect('list_tareas')

def create_tipo_recurso(request):
    if request.method == 'POST':
        tipo_r = request.POST['tipo_r']
        TblTipoR.objects.create(tipo_r=tipo_r)
        return redirect('list_tipo_recursos')

    return render(request, 'tipo_recurso.html')
def list_tipo_recursos(request):
    tipo_recursos = TblTipoR.objects.all()
    return render(request, 'tipo_recurso.html', {'tipo_recursos': tipo_recursos})
def edit_tipo_recurso(request, tipo_r_id):
    tipo_recurso = get_object_or_404(TblTipoR, id=tipo_r_id)

    if request.method == 'POST':
        tipo_recurso.tipo_r = request.POST['tipo_r']
        tipo_recurso.save()
        return redirect('list_tipo_recursos')

    return render(request, 'edit_tipo_recurso.html', {'tipo_recurso': tipo_recurso})
def delete_tipo_recurso(request):
    if request.method == 'POST':
        tipo_r_id = request.POST['tipo_r_id']
        tipo_recurso = get_object_or_404(TblTipoR, id=tipo_r_id)
        tipo_recurso.delete()
        return redirect('list_tipo_recursos')

    return redirect('list_tipo_recursos')

def create_unidad(request):
    if request.method == 'POST':
        unidad = request.POST['unidad']
        TblUnidadM.objects.create(unidad=unidad)
        return redirect('list_unidades')

    return render(request, 'unidad.html')
def list_unidades(request):
    unidades = TblUnidadM.objects.all()
    return render(request, 'unidad.html', {'unidades': unidades})
def edit_unidad(request, unidad_id):
    unidad = get_object_or_404(TblUnidadM, id=unidad_id)

    if request.method == 'POST':
        unidad.unidad = request.POST['unidad']
        unidad.save()
        return redirect('list_unidades')

    return render(request, 'edit_unidad.html', {'unidad': unidad})
def delete_unidad(request):
    if request.method == 'POST':
        unidad_id = request.POST['unidad_id']
        unidad = get_object_or_404(TblUnidadM, id=unidad_id)
        unidad.delete()
        return redirect('list_unidades')

    return redirect('list_unidades')

def create_personal(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre_personal = request.POST['nombre_personal']
        apell_personal = request.POST['apell_personal']
        telefono_p = request.POST.get('telefono_p')
        cargo_p = request.POST['cargo_p']
        nom_referencia = request.POST.get('nom_referencia')
        vinculo = request.POST.get('vinculo')
        telefono_r = request.POST.get('telefono_r')
        direccion_p = request.POST.get('direccion_p')
        departamento_p = request.POST.get('departamento_p')
        provincia_p = request.POST.get('provincia_p')
        distrito_p = request.POST.get('distrito_p')

        # Crear un nuevo objeto TblPersonal y guardarlo en la base de datos
        TblPersonal.objects.create(
            nombre_personal=nombre_personal,
            apell_personal=apell_personal,
            telefono_p=telefono_p,
            cargo_p=cargo_p,
            nom_referencia=nom_referencia,
            vinculo=vinculo,
            telefono_r=telefono_r,
            direccion_p=direccion_p,
            departamento_p=departamento_p,
            provincia_p=provincia_p,
            distrito_p=distrito_p
        )
        return redirect('list_personal')

    return render(request, 'crear_personal.html')
def list_personal(request):
    # Obtener todos los registros de TblPersonal de la base de datos
    personal = TblPersonal.objects.all()
    return render(request, 'personal.html', {'personal': personal})
def edit_personal(request, personal_id):
    # Obtener el objeto TblPersonal correspondiente al ID proporcionado
    personal = get_object_or_404(TblPersonal, id=personal_id)

    if request.method == 'POST':
        # Obtener datos del formulario
        nombre_personal = request.POST['nombre_personal']
        apell_personal = request.POST['apell_personal']
        telefono_p = request.POST.get('telefono_p')
        cargo_p = request.POST['cargo_p']
        nom_referencia = request.POST.get('nom_referencia')
        vinculo = request.POST.get('vinculo')
        telefono_r = request.POST.get('telefono_r')
        direccion_p = request.POST.get('direccion_p')
        departamento_p = request.POST.get('departamento_p')
        provincia_p = request.POST.get('provincia_p')
        distrito_p = request.POST.get('distrito_p')

        # Actualizar los datos del objeto personal
        personal.nombre_personal = nombre_personal
        personal.apell_personal = apell_personal
        personal.telefono_p = telefono_p
        personal.cargo_p = cargo_p
        personal.nom_referencia = nom_referencia
        personal.vinculo = vinculo
        personal.telefono_r = telefono_r
        personal.direccion_p = direccion_p
        personal.departamento_p = departamento_p
        personal.provincia_p = provincia_p
        personal.distrito_p = distrito_p

        # Guardar los cambios en la base de datos
        personal.save()

        return redirect('list_personal')

    return render(request, 'edit_personal.html', {'personal': personal})
def delete_personal(request):
    if request.method == 'POST':
        personal_id = request.POST.get('personal_id')
        personal = get_object_or_404(TblPersonal, id=personal_id)

        # Verificar si hay registros asociados en el otro modelo usando la ForeignKey 'personal_id'
        if TblRecurso.objects.filter(num_factura_idp=personal_id).exists():
            messages.error(request, 'No puedes eliminar este personal porque está siendo utilizado en otros recursos.')
        else:
            personal.delete()
            messages.success(request, 'El personal ha sido eliminado exitosamente.')

    return redirect('list_personal')


def create_recurso(request):
    if request.method == 'POST':
        id_tarea = request.POST['tarea']
        id_tipo_r_value = request.POST['tipo_recurso']

        # Obtener el ID del tipo de recurso a partir de su valor (buscándolo en la base de datos)
        tipo_recurso = get_object_or_404(TblTipoR, tipo_r=id_tipo_r_value)
        id_tipo_r = tipo_recurso.id

        cantidad = request.POST.get('cantidad')
        id_unidad_m = request.POST.get('unidad_medida')
        precio = request.POST.get('precio')

        # Obtener el detalle o el personal_id dependiendo del tipo de recurso seleccionado
        detalle_nom_p = request.POST.get('detalle_nom_p')
        num_factura_idp = request.POST.get('numero_factura')

        if id_tipo_r_value == 'Humano':
            personal_id = request.POST.get('personal_id')
            # Obtener el objeto TblPersonal correspondiente al ID proporcionado
            personal = get_object_or_404(TblPersonal, id=personal_id)
            detalle_nom_p = f"{personal.nombre_personal} {personal.apell_personal}"
            num_factura_idp = personal_id

        with transaction.atomic():
            # Utilizar atomic transaction para asegurar que se guarden todos los datos o ninguno en caso de error
            TblRecurso.objects.create(
                id_tarea_id=id_tarea,
                id_tipo_r_id=id_tipo_r,
                detalle_nom_p=detalle_nom_p,
                num_factura_idp=num_factura_idp,
                cantidad=cantidad,
                id_unidad_m_id=id_unidad_m,
                precio=precio
            )
        return redirect('list_recursos')

    tareas = TblTarea.objects.all()
    tipos_recurso = TblTipoR.objects.all()
    unidades_medida = TblUnidadM.objects.all()
    personal_list = TblPersonal.objects.all()

    return render(request, 'crear_recurso.html', {
        'tareas': tareas,
        'tipos_recurso': tipos_recurso,
        'unidades_medida': unidades_medida,
        'personal_list': personal_list,
    })
def list_recursos(request):
    recursos = TblRecurso.objects.all()
    return render(request, 'recurso.html', {'recursos': recursos})

def edit_recurso(request, recurso_id):
    recurso = get_object_or_404(TblRecurso, id=recurso_id)

    if request.method == 'POST':
        id_tarea = request.POST['tarea']
        id_tipo_r = request.POST['tipo_recurso']
        detalle_nom_p = request.POST.get('detalle_nombre')
        num_factura_idp = request.POST.get('numero_factura')
        cantidad = request.POST.get('cantidad')
        id_unidad_m = request.POST.get('unidad_medida')
        precio = request.POST.get('precio')

        recurso.id_tarea_id = id_tarea
        recurso.id_tipo_r_id = id_tipo_r
        recurso.detalle_nom_p = detalle_nom_p
        recurso.num_factura_idp = num_factura_idp
        recurso.cantidad = cantidad
        recurso.id_unidad_m_id = id_unidad_m
        recurso.precio = precio

        recurso.save()

        return redirect('list_recursos')

    tareas = TblTarea.objects.all()
    tipos_recurso = TblTipoR.objects.all()
    unidades_medida = TblUnidadM.objects.all()

    return render(request, 'edit_recurso.html', {
        'recurso': recurso,
        'tareas': tareas,
        'tipos_recurso': tipos_recurso,
        'unidades_medida': unidades_medida,
    })

def delete_recurso(request):
    if request.method == 'POST':
        recurso_id = request.POST.get('recurso_id')
        recurso = get_object_or_404(TblRecurso, id=recurso_id)
        recurso.delete()
        return redirect('list_recursos')

    return redirect('list_recursos')