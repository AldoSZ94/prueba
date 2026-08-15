from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        clases = (
            "w-full px-4 py-2.5 "
            "text-sm text-slate-900 "
            "bg-white border border-slate-300 rounded-lg "
            "placeholder:text-slate-400 "
            "focus:outline-none focus:ring-2 focus:ring-slate-300 "
            "focus:border-slate-400 "
            "transition-colors duration-200"
        )

        self.fields["username"].widget.attrs.update(
            {
                "class": clases,
                "placeholder": "Escribe tu usuario",
                "autocomplete": "username",
            }
        )

        self.fields["password1"].widget.attrs.update(
            {
                "class": clases,
                "placeholder": "Crea una contraseña",
                "autocomplete": "new-password",
            }
        )

        self.fields["password2"].widget.attrs.update(
            {
                "class": clases,
                "placeholder": "Repite tu contraseña",
                "autocomplete": "new-password",
            }
        )


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update(
            {
                "class": "w-full px-3 py-2 text-sm border border-slate-300 rounded-lg "
                "focus:outline-none focus:ring-2 focus:ring-slate-400 "
                "focus:border-slate-400 transition"
            }
        )

        self.fields["password"].widget.attrs.update(
            {
                "class": "w-full px-3 py-2 text-sm border border-slate-300 rounded-lg "
                "focus:outline-none focus:ring-2 focus:ring-slate-400 "
                "focus:border-slate-400 transition"
            }
        )
