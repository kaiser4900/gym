from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from django.forms import widgets
from .models import User,Usuario,Niveles


class UsuarioSignUpForm(UserCreationForm):
    

    first_name    = forms.CharField(required=True, widget= forms.TextInput(attrs={'class':"form-control"}))
    last_name     = forms.CharField(required=True, widget= forms.TextInput(attrs={'class':"form-control"}))
    email         = forms.EmailField(required=True, widget= forms.TextInput(attrs={'class':"form-control"}))

    level         = forms.ModelChoiceField(queryset=Niveles.objects.all(),empty_label='Nivel')
    level.widget.attrs.update({'class':"fdropdown-toggle btn btn-primary btn-block"})

    dni           = forms.IntegerField(required=True, widget= forms.NumberInput(attrs={'class':"form-control"}))
    image         = forms.ImageField(required=True, widget= forms.FileInput(attrs={'class':"form-control"}))
    peso          = forms.FloatField(required=True, widget= forms.NumberInput(attrs={'class':"form-control"}))
    altura        = forms.FloatField(required=True, widget= forms.NumberInput(attrs={'class':"form-control"}))
    direccion     = forms.CharField(required=True, widget= forms.TextInput(attrs={'class':"form-control"}))
    descripcion   = forms.CharField(widget= forms.Textarea(attrs={'class':"form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','type':'password', 'name': 'password1','placeholder':'Password'}),
    label='')

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','type':'password', 'name': 'password2','placeholder':'Password'}),
    label='')

    class Meta(UserCreationForm.Meta):
        model = User
        widgets = {
            "username": widgets.TextInput(attrs={'class':"form-control"}),
        }

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        
        user.first_name    = self.cleaned_data.get('first_name')
        user.last_name     = self.cleaned_data.get('last_name')
        user.email         = self.cleaned_data.get('email')
        user.level         = self.cleaned_data.get('level')
        user.dni           = self.cleaned_data.get('dni')
        user.image         = self.cleaned_data.get('image')

        user.save()
        usuario= Usuario.objects.create(
            user=user,
            peso = self.cleaned_data.get('peso'),
            altura = self.cleaned_data.get('altura'),
            direccion = self.cleaned_data.get('direccion'),
            descripcion = self.cleaned_data.get('descripcion'),
        )

        return user