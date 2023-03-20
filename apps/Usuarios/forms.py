from . import models
from django import forms
#from bootstrap_modal_forms.forms import BSModalModelForm




class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "class": "text-field w-input"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "text-field-2 w-input"}
        )
    )
