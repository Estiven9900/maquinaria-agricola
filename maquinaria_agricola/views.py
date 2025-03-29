from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.forms import modelform_factory
from .models import Maquina, Complemento, Trabajador, Operacion

# Vistas para Máquinas
def maquina_list(request):
    maquinas = Maquina.objects.all()
    return render(request, 'maquina_list.html', {'maquinas': maquinas})

def maquina_create(request):
    MaquinaForm = modelform_factory(Maquina, fields='__all__')
    if request.method == 'POST':
        form = MaquinaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Máquina creada exitosamente')
            return redirect('maquina_list')
    else:
        form = MaquinaForm()
    return render(request, 'maquina_form.html', {'form': form, 'title': 'Crear Máquina'})

def maquina_update(request, pk):
    maquina = get_object_or_404(Maquina, pk=pk)
    MaquinaForm = modelform_factory(Maquina, fields='__all__')
    if request.method == 'POST':
        form = MaquinaForm(request.POST, instance=maquina)
        if form.is_valid():
            form.save()
            messages.success(request, 'Máquina actualizada exitosamente')
            return redirect('maquina_list')
    else:
        form = MaquinaForm(instance=maquina)
    return render(request, 'maquina_form.html', {'form': form, 'title': 'Editar Máquina'})

def maquina_delete(request, pk):
    maquina = get_object_or_404(Maquina, pk=pk)
    if request.method == 'POST':
        maquina.delete()
        messages.success(request, 'Máquina eliminada exitosamente')
        return redirect('maquina_list')
    return render(request, 'maquina_confirm_delete.html', {'maquina': maquina})

# Vistas para Complementos
def complemento_list(request):
    complementos = Complemento.objects.all()
    return render(request, 'complemento_list.html', {'complementos': complementos})

def complemento_create(request):
    ComplementoForm = modelform_factory(Complemento, fields='__all__')
    if request.method == 'POST':
        form = ComplementoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Complemento creado exitosamente')
            return redirect('complemento_list')
    else:
        form = ComplementoForm()
    return render(request, 'complemento_form.html', {'form': form, 'title': 'Crear Complemento'})

def complemento_update(request, pk):
    complemento = get_object_or_404(Complemento, pk=pk)
    ComplementoForm = modelform_factory(Complemento, fields='__all__')
    if request.method == 'POST':
        form = ComplementoForm(request.POST, instance=complemento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Complemento actualizado exitosamente')
            return redirect('complemento_list')
    else:
        form = ComplementoForm(instance=complemento)
    return render(request, 'complemento_form.html', {'form': form, 'title': 'Editar Complemento'})

def complemento_delete(request, pk):
    complemento = get_object_or_404(Complemento, pk=pk)
    if request.method == 'POST':
        complemento.delete()
        messages.success(request, 'Complemento eliminado exitosamente')
        return redirect('complemento_list')
    return render(request, 'complemento_confirm_delete.html', {'complemento': complemento})

# Vistas para Trabajadores
def trabajador_list(request):
    trabajadores = Trabajador.objects.all()
    return render(request, 'trabajador_list.html', {'trabajadores': trabajadores})

def trabajador_create(request):
    TrabajadorForm = modelform_factory(Trabajador, fields='__all__')
    if request.method == 'POST':
        form = TrabajadorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Trabajador creado exitosamente')
            return redirect('trabajador_list')
    else:
        form = TrabajadorForm()
    return render(request, 'trabajador_form.html', {'form': form, 'title': 'Crear Trabajador'})

def trabajador_update(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    TrabajadorForm = modelform_factory(Trabajador, fields='__all__')
    if request.method == 'POST':
        form = TrabajadorForm(request.POST, instance=trabajador)
        if form.is_valid():
            form.save()
            messages.success(request, 'Trabajador actualizado exitosamente')
            return redirect('trabajador_list')
    else:
        form = TrabajadorForm(instance=trabajador)
    return render(request, 'trabajador_form.html', {'form': form, 'title': 'Editar Trabajador'})

def trabajador_delete(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    if request.method == 'POST':
        trabajador.delete()
        messages.success(request, 'Trabajador eliminado exitosamente')
        return redirect('trabajador_list')
    return render(request, 'trabajador_confirm_delete.html', {'trabajador': trabajador})

# Vistas para Operaciones
def operacion_list(request):
    operaciones = Operacion.objects.all()
    return render(request, 'operacion_list.html', {'operaciones': operaciones})

def operacion_create(request):
    OperacionForm = modelform_factory(Operacion, fields='__all__')
    if request.method == 'POST':
        form = OperacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Operación creada exitosamente')
            return redirect('operacion_list')
    else:
        form = OperacionForm()
    return render(request, 'operacion_form.html', {'form': form, 'title': 'Crear Operación'})

def operacion_update(request, pk):
    operacion = get_object_or_404(Operacion, pk=pk)
    OperacionForm = modelform_factory(Operacion, fields='__all__')
    if request.method == 'POST':
        form = OperacionForm(request.POST, instance=operacion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Operación actualizada exitosamente')
            return redirect('operacion_list')
    else:
        form = OperacionForm(instance=operacion)
    return render(request, 'operacion_form.html', {'form': form, 'title': 'Editar Operación'})

def operacion_delete(request, pk):
    operacion = get_object_or_404(Operacion, pk=pk)
    if request.method == 'POST':
        operacion.delete()
        messages.success(request, 'Operación eliminada exitosamente')
        return redirect('operacion_list')
    return render(request, 'operacion_confirm_delete.html', {'operacion': operacion})