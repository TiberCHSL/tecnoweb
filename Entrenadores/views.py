from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django.views.generic import ListView
from .forms import UserForm, ClienteForm, EntrenadorForm,ModalidadForm, LugarTrabajoForm, EquipamientoForm, EspecializacionForm, EducacionForm, ExperienciaForm
from .models import Cliente, Entrenador, Modalidad, LugarTrabajo, Equipamiento, Especializacion, Experiencia, ImgEntr, AvatarEntr
from.decorators import is_entrenador, is_cliente
from django.shortcuts import render, get_object_or_404

def registration_selection(request):
    return render(request, 'registration_selection.html')

def register_cliente(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        cliente_form = ClienteForm(request.POST)
        if user_form.is_valid() and cliente_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            
            cliente = cliente_form.save(commit=False)
            cliente.user = user
            cliente.save()
            
            login(request, user)
            return redirect('clientes_view')  # Replace 'home' with your desired redirect URL
    else:
        user_form = UserForm()
        cliente_form = ClienteForm()
    return render(request, 'register_cliente.html', {'user_form': user_form, 'cliente_form': cliente_form})

def register_entrenador(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        entrenador_form = EntrenadorForm(request.POST)
        if user_form.is_valid() and entrenador_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            
            entrenador = entrenador_form.save(commit=False)
            entrenador.user = user
            entrenador.save()
            
            login(request, user)
            return redirect('add_modalidades')  # Redirect to follow-up form
    else:
        user_form = UserForm()
        entrenador_form = EntrenadorForm()
    return render(request, 'register_entrenador.html', {'user_form': user_form, 'entrenador_form': entrenador_form})


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if Entrenador.objects.filter(user=user).exists():
                    return redirect('entrenadores_view')
                elif Cliente.objects.filter(user=user).exists():
                    return redirect('clientes_view')
                else:
                    return redirect('login')  # Loop back to login view if neither condition is met
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('registration_selection')

def add_modalidades(request):
    if request.method == 'POST':
        form = ModalidadForm(request.POST)
        if form.is_valid():
            modalidades_selected = form.cleaned_data['nombre_modalidad']
            entrenador = request.user.entrenador  # Assuming the user is authenticated and linked to an Entrenador instance
            
            # Clear existing modalidades to avoid duplicates
            entrenador.Modalidades.clear()  # Use Modalidades as per the related_name
            
            # Add newly selected modalidades
            for modalidad in modalidades_selected:
                modalidad_obj, created = Modalidad.objects.get_or_create(nombre_modalidad=modalidad)
                entrenador.Modalidades.add(modalidad_obj)  # Use Modalidades as per the related_name
            
            # Inside add_modalidades view, after saving modalidades_selected

            if 'PR' in modalidades_selected:
                return redirect('add_lugares_trabajo')  # Redirect to adding lugares de trabajo if "Presencial" is selected
            else:
                return redirect('add_especializaciones')  # Or wherever you'd normally redirect 
    else:
        form = ModalidadForm()

    return render(request, 'add_modalidades.html', {'form': form})

def add_lugares_trabajo(request):
    if request.method == 'POST':
        form = LugarTrabajoForm(request.POST)
        if form.is_valid():
            lugares_selected = form.cleaned_data['lugares']
            entrenador = request.user.entrenador  # Assuming the user is authenticated and linked to an Entrenador instance
            
            # Clear existing lugares to avoid duplicates
            entrenador.Lugares_trabajo.clear()
            
            # Add newly selected lugares
            for lugar in lugares_selected:
                lugar_trabajo, created = LugarTrabajo.objects.get_or_create(name=lugar)
                entrenador.Lugares_trabajo.add(lugar_trabajo)
            
            # Check if any of the selected lugares are 'AL' or 'DO' directly in lugares_selected
            if any(lugar in ['AL', 'DO'] for lugar in lugares_selected):
                return redirect('add_equipamientos')  # Redirect to add_equipamientos if 'AL' or 'DO' is selected
            else:
                return redirect('add_especializaciones')  # Redirect to another view if none of 'AL' or 'DO' is selected
    else:
        form = LugarTrabajoForm()

    return render(request, 'add_lugares_trabajo.html', {'form': form})

def add_equipamientos(request):
    if request.method == 'POST':
        form = EquipamientoForm(request.POST)
        if form.is_valid():
            equipamientos_selected = form.cleaned_data['equipamientos']
            entrenador = request.user.entrenador  # Assuming the user is authenticated and linked to an Entrenador instance
            
            # Clear existing equipamientos to avoid duplicates
            entrenador.Equipamiento.clear()
            
            # Add newly selected equipamientos
            for equipamiento in equipamientos_selected:
                equipamiento_obj, created = Equipamiento.objects.get_or_create(name=equipamiento)
                entrenador.Equipamiento.add(equipamiento_obj)
            
            return redirect('add_especializaciones')  # Redirect to a suitable page after adding equipamientos
    else:
        form = EquipamientoForm()

    return render(request, 'add_equipamientos.html', {'form': form})

# views.py

def add_especializaciones(request):
    if request.method == 'POST':
        form = EspecializacionForm(request.POST)
        if form.is_valid():
            especializaciones_selected = form.cleaned_data['especializaciones']
            entrenador = request.user.entrenador  # Assuming the user is authenticated and linked to an Entrenador instance
            
            # Clear existing especializaciones to avoid duplicates
            entrenador.Especializacion.clear()
            
            # Add newly selected especializaciones
            for especializacion in especializaciones_selected:
                especializacion_obj, created = Especializacion.objects.get_or_create(nombre_esp=especializacion)
                entrenador.Especializacion.add(especializacion_obj)
            
            return redirect('add_educacion')  # Redirect to a suitable page after adding especializaciones
    else:
        form = EspecializacionForm()

    return render(request, 'add_especializaciones.html', {'form': form})


from django.forms import formset_factory

def add_educacion(request):
    EducacionFormSet = formset_factory(EducacionForm, extra=1, max_num=10)
    
    if request.method == 'POST':
        formset = EducacionFormSet(request.POST, prefix='educacion')
        print("Total forms:", len(formset))  # Print total number of forms received
        valid_forms_count = sum(1 for form in formset if form.is_valid())
        print("Valid forms:", valid_forms_count)  # Count and print the number of valid forms
        
        for form in formset:
            if form.is_valid():
                print("Saving form")  # Indicate when a form is being saved
                educacion = form.save(commit=False)  # Get an unsaved instance from the form
                educacion.rut_en = request.user.entrenador
                educacion.save()  # Now save each instance after modification
                print("Form saved")  # Confirm the form is 
            else:
                print(formset.errors)
        else:
            print("Invalid form detected")  # Indicate when a form is invalid
        return redirect('add_experiencia')
    else:
        formset = EducacionFormSet(prefix='educacion')
    
    return render(request, 'add_educacion.html', {'formset': formset})

def add_experiencia(request):
    if request.method == 'POST':
        form = ExperienciaForm(request.POST)
        if form.is_valid():
            experiencia = form.save(commit=False)
            experiencia.rut_en = request.user.entrenador  # Assuming the user is authenticated and linked to an Entrenador instance
            experiencia.save()
            return redirect('entrenadores_view')  # Redirect to the list of experiencias or wherever appropriate
    else:
        form = ExperienciaForm()

    return render(request, 'add_experiencia.html', {'form': form})
    
@login_required
@is_entrenador
def entrenadores_view(request):
    return render(request, 'entrenadores_dashboard.html')

@login_required
@is_cliente
def clientes_view(request):
    return render(request, 'clientes_dashboard.html')

class TrainerListView(ListView):
    model = Entrenador
    template_name = 'trainer_list.html'
    context_object_name = 'trainers'

    def get_queryset(self):
        return Entrenador.objects.all()


def trainer_list(request):
    trainers = Entrenador.objects.all()
    return render(request, 'trainer_list.html', {'trainers': trainers})

def trainer_detail(request, trainer_rut):
    trainer = get_object_or_404(Entrenador, rut_en=trainer_rut)
    images = ImgEntr.objects.filter(rut_en=trainer)
    modalities = trainer.Modalidades.values_list('nombre_modalidad', flat=True)
    return render(request, 'trainer_detail.html', {'trainer': trainer, 'images': images, 'modalities': modalities})