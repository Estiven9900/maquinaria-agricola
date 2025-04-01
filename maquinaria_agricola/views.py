from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Maquina, Complemento, Trabajador, Operacion
from .forms import MaquinaForm, ComplementoForm, TrabajadorForm, OperacionForm

def home(request):
    return render(request, 'home.html')

@login_required
@permission_required('maquinaria_agricola.view_maquina', raise_exception=True)
def maquina_list(request):
    maquinas = Maquina.objects.all()
    print("Máquinas encontradas:", maquinas)  # Agrega esto para depurar
    return render(request, 'maquinaria_agricola/maquina_list.html', {'maquinas': maquinas})

@login_required
@permission_required('maquinaria_agricola.add_maquina', raise_exception=True)
def maquina_create(request):
    if request.method == 'POST':
        form = MaquinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maquina_list')
    else:
        form = MaquinaForm()
    return render(request, 'maquinaria_agricola/maquina_form.html', {'form': form})

@login_required
@permission_required('maquinaria_agricola.change_maquina', raise_exception=True)
def maquina_update(request, pk):
    maquina = get_object_or_404(Maquina, pk=pk)
    if request.method == 'POST':
        form = MaquinaForm(request.POST, instance=maquina)
        if form.is_valid():
            form.save()
            return redirect('maquina_list')
    else:
        form = MaquinaForm(instance=maquina)
    return render(request, 'maquinaria_agricola/maquina_form.html', {'form': form})

@login_required
@permission_required('maquinaria_agricola.delete_maquina', raise_exception=True)
def maquina_delete(request, pk):
    maquina = get_object_or_404(Maquina, pk=pk)
    if request.method == 'POST':
        maquina.delete()
        return redirect('maquina_list')
    return render(request, 'maquinaria_agricola/maquina_confirm_delete.html', {'maquina': maquina})

@login_required
@permission_required('maquinaria_agricola.view_complemento', raise_exception=True)
def complemento_list(request):
    complementos = Complemento.objects.all()
    print("Complementos encontrados:", complementos)  # Agrega esto para depurar
    return render(request, 'maquinaria_agricola/complemento_list.html', {'complementos': complementos})

@login_required
@permission_required('maquinaria_agricola.add_complemento', raise_exception=True)
def complemento_create(request):
    if request.method == 'POST':
        form = ComplementoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('complemento_list')
    else:
        form = ComplementoForm()
    return render(request, 'maquinaria_agricola/complemento_form.html', {'form': form})

@login_required
@permission_required('maquinaria_agricola.change_complemento', raise_exception=True)
def complemento_update(request, pk):
    complemento = get_object_or_404(Complemento, pk=pk)
    if request.method == 'POST':
        form = ComplementoForm(request.POST, instance=complemento)
        if form.is_valid():
            form.save()
            return redirect('complemento_list')
    else:
        form = ComplementoForm(instance=complemento)
    return render(request, 'maquinaria_agricola/complemento_form.html', {'form': form})

@login_required
@permission_required('maquinaria_agricola.delete_complemento', raise_exception=True)
def complemento_delete(request, pk):
    complemento = get_object_or_404(Complemento, pk=pk)
    if request.method == 'POST':
        complemento.delete()
        return redirect('complemento_list')
    return render(request, 'maquinaria_agricola/complemento_confirm_delete.html', {'complemento': complemento})

@login_required
@permission_required('maquinaria_agricola.view_trabajador', raise_exception=True)
def trabajador_list(request):
    trabajadores = Trabajador.objects.all()
    print("Trabajadores encontrados:", trabajadores)  # Agrega esto para depurar
    return render(request, 'maquinaria_agricola/trabajador_list.html', {'trabajadores': trabajadores})

@login_required
@permission_required('maquinaria_agricola.add_trabajador', raise_exception=True)
def trabajador_create(request):
    if request.method == 'POST':
        form = TrabajadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trabajador_list')
    else:
        form = TrabajadorForm()
    return render(request, 'maquinaria_agricola/trabajador_form.html', {'form': form})

@login_required
@permission_required('maquinaria_agricola.change_trabajador', raise_exception=True)
def trabajador_update(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    if request.method == 'POST':
        form = TrabajadorForm(request.POST, instance=trabajador)
        if form.is_valid():
            form.save()
            return redirect('trabajador_list')
    else:
        form = TrabajadorForm(instance=trabajador)
    return render(request, 'maquinaria_agricola/trabajador_form.html', {'form': form})

@login_required
@permission_required('maquinaria_agricola.delete_trabajador', raise_exception=True)
def trabajador_delete(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    if request.method == 'POST':
        trabajador.delete()
        return redirect('trabajador_list')
    return render(request, 'maquinaria_agricola/trabajador_confirm_delete.html', {'trabajador': trabajador})

@login_required
@permission_required('maquinaria_agricola.view_operacion', raise_exception=True)
def operacion_list(request):
    operaciones = Operacion.objects.all()
    print("Operaciones encontradas:", operaciones)  # Agrega esto para depurar
    return render(request, 'maquinaria_agricola/operacion_list.html', {'operaciones': operaciones})

@login_required
@permission_required('maquinaria_agricola.add_operacion', raise_exception=True)
def operacion_create(request):
    if request.method == 'POST':
        form = OperacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('operacion_list')
    else:
        form = OperacionForm()
    return render(request, 'maquinaria_agricola/operacion_form.html', {'form': form})

@login_required
@permission_required('maquinaria_agricola.change_operacion', raise_exception=True)
def operacion_update(request, pk):
    operacion = get_object_or_404(Operacion, pk=pk)
    if request.method == 'POST':
        form = OperacionForm(request.POST, instance=operacion)
        if form.is_valid():
            form.save()
            return redirect('operacion_list')
    else:
        form = OperacionForm(instance=operacion)
    return render(request, 'maquinaria_agricola/operacion_form.html', {'form': form})

@login_required
@permission_required('maquinaria_agricola.delete_operacion', raise_exception=True)
def operacion_delete(request, pk):
    operacion = get_object_or_404(Operacion, pk=pk)
    if request.method == 'POST':
        operacion.delete()
        return redirect('operacion_list')
    return render(request, 'maquinaria_agricola/operacion_confirm_delete.html', {'operacion': operacion})