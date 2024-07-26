from .models import Cliente, Entrenador, Modalidad, LugarTrabajo, Equipamiento, Especializacion, Educacion, Experiencia
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class ClienteForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Cliente
        fields = ['phone', 'rut_cl', 'birth_date', 'gender']

class EntrenadorForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Entrenador
        fields = ['phone', 'rut_en', 'birth_date', 'gender']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'password', 'email']

class EntrenadorFollowUpForm(forms.ModelForm):
    class Meta:
        model = Entrenador
        fields = ['direccion']


class ModalidadForm(forms.Form):
    MODALIDAD_CHOICES = [
        ('OL', 'Online'),
        ('PR', 'Presencial'),
    ]

    nombre_modalidad = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=MODALIDAD_CHOICES,
        required=False,
    )

class LugarTrabajoForm(forms.Form):
    lugares_choices = [(choice[0], choice[1]) for choice in LugarTrabajo.NAME_CHOICES]

    lugares = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=lugares_choices,
        required=False,
    )

class EquipamientoForm(forms.Form):
    equipamiento_choices = [(choice[0], choice[1]) for choice in Equipamiento.NAME_CHOICES]

    equipamientos = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=equipamiento_choices,
        required=False,
    )

class EspecializacionForm(forms.Form):
    especializacion_choices = [(choice[0], choice[1]) for choice in Especializacion.ESPECIALIZACION_CHOICES]

    especializaciones = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=especializacion_choices,
        required=False,
    )

class EducacionForm(forms.ModelForm):
    class Meta:
        model = Educacion
        exclude = ['rut_en']


from django import forms
from .models import Experiencia

class ExperienciaForm(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = ['cargo', 'anos_exp', 'desc']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['desc'].widget = forms.Textarea(
            attrs={
                'rows': 10,
                'cols': 100,
                'class': 'form-control materialize-textarea',
                'required': True,
                'data-validation-required-message': 'Please enter your message',
                'minlength': 5,
                'data-validation-minlength-message': 'Min 5 characters',
                'maxlength': 999,
                'style': 'resize:none'
            }
        )
