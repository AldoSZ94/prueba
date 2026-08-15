from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tarea
from .forms import TareaForm


@login_required
def lista_tareas(request):
    tareas = Tarea.objects.filter(usuario=request.user)
    return render(request, "tareas/lista_tareas.html", {"tareas": tareas})


@login_required
def nueva_tarea(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.usuario = request.user
            tarea.save()
            return redirect("tareas:lista_tareas")
    else:
        form = TareaForm()
    return render(
        request, "tareas/formulario.html", {"form": form, "accion": "Agregar"}
    )


@login_required
def editar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id, usuario=request.user)
    if request.method == "POST":
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect("tareas:lista_tareas")
    else:
        form = TareaForm(instance=tarea)
    return render(request, "tareas/formulario.html", {"form": form, "accion": "Editar"})


@login_required
def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id, usuario=request.user)
    if request.method == "POST":
        tarea.delete()
        return redirect("tareas:lista_tareas")
    return render(request, "tareas/eliminar_tarea.html", {"tarea": tarea})
