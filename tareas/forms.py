from datetime import date

from django import forms
from .models import Tarea


class TareaForm(forms.ModelForm):

    class Meta:
        model = Tarea
        fields = [
            "titulo",
            "descripcion",
            "prioridad",
            "fecha_limite",
            "completado",
        ]

        widgets = {
            "titulo": forms.TextInput(
                attrs={
                    "placeholder": "Título de la tarea",
                    "class": (
                        "w-full px-3 py-2 text-sm border border-slate-300 "
                        "rounded-lg focus:outline-none focus:ring-2 "
                        "focus:ring-slate-400 focus:border-slate-400 "
                        "transition"
                    ),
                }
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "placeholder": "Descripción de la tarea",
                    "rows": 6,
                    "class": (
                        "w-full px-3 py-2 text-sm border border-slate-300 "
                        "rounded-lg focus:outline-none focus:ring-2 "
                        "focus:ring-slate-400 focus:border-slate-400 "
                        "transition resize-none"
                    ),
                }
            ),
            "prioridad": forms.Select(
                attrs={
                    "class": (
                        "w-full px-3 py-2 text-sm border border-slate-300 "
                        "rounded-lg bg-white focus:outline-none "
                        "focus:ring-2 focus:ring-slate-400 "
                        "focus:border-slate-400 transition"
                    ),
                }
            ),
            "fecha_limite": forms.DateInput(
                attrs={
                    "type": "date",
                    "min": date.today().isoformat(),
                    "class": (
                        "w-full px-3 py-2 text-sm border border-slate-300 "
                        "rounded-lg bg-white focus:outline-none "
                        "focus:ring-2 focus:ring-slate-400 "
                        "focus:border-slate-400 transition"
                    ),
                }
            ),
            "completado": forms.CheckboxInput(
                attrs={
                    "class": (
                        "w-4 h-4 text-slate-800 border-slate-300 "
                        "rounded focus:ring-2 focus:ring-slate-400"
                    ),
                }
            ),
        }


# from datetime import date
# from django import forms
# from .models import Tarea


# class TareaForm(forms.ModelForm):

#     class Meta:
#         model = Tarea
#         fields = ["titulo", "descripcion", "prioridad", "fecha_limite", "completado"]
#         widgets = {
#             "titulo": forms.TextInput(attrs={"placeholder": "Título de la Tarea"}),
#             "descripcion": forms.Textarea(
#                 attrs={"placeholder": "Descripción de la Tarea"}
#             ),
#             "prioridad": forms.Select(),
#             "fecha_limite": forms.DateInput(
#                 attrs={"type": "date", "min": date.today().isoformat()}
#             ),
#             "completado": forms.CheckboxInput(),
#         }
