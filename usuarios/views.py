from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegistroForm, LoginForm


def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("usuarios:iniciar_sesion")

    else:
        form = RegistroForm()

    return render(request, "usuarios/registro.html", {"form": form})


def iniciar_sesion(request):
    if request.method == "POST":
        form = LoginForm(request, request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect("tareas:lista_tareas")

    else:
        form = LoginForm(request)

    return render(request, "usuarios/iniciar_sesion.html", {"form": form})


def cerrar_sesion(request):
    logout(request)
    return redirect("usuarios:iniciar_sesion")


# from django.shortcuts import render, redirect
# from django.contrib.auth import login, logout
# from django.contrib.auth.forms import AuthenticationForm
# from .forms import RegistroForm


# def registro(request):
#     if request.method == "POST":
#         form = RegistroForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("usuarios:iniciar_sesion")
#     else:
#         form = RegistroForm()
#     return render(request, "usuarios/registro.html", {"form": form})


# def iniciar_sesion(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             login(request, form.get_user())
#             return redirect("tareas:lista_tareas")
#     else:
#         form = AuthenticationForm()
#     return render(request, "usuarios/iniciar_sesion.html", {"form": form})


# def cerrar_sesion(request):
#     logout(request)
#     return redirect("usuarios:iniciar_sesion")
