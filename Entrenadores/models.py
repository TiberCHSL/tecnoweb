from django.db import models
from django.contrib.auth.models import User
#from d3_dpa_chile.models import Region, Provincia, Comuna

# Create your models here.
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name = "Nombre de usuario")
    phone = models.CharField(max_length=20, verbose_name="Teléfono", null = True)
    rut_cl = models.CharField(primary_key=True, max_length=12, verbose_name="RUT")
    birth_date = models.DateField(verbose_name="Fecha de Nacimiento", null=True, blank=True)
    gender = models.CharField(max_length=10, verbose_name="Género", choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')])
    role = models.CharField(max_length=10, verbose_name="Rol de usuario", choices=[('C', 'Cliente')], default= 'C')
    #comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user)
    
class Entrenador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name = "Nombre de usuario")
    phone = models.CharField(max_length=20, verbose_name="Teléfono", null = True)
    rut_en = models.CharField(primary_key=True, max_length=12, verbose_name="RUT")
    birth_date = models.DateField(verbose_name="Fecha de Nacimiento", null=True, blank=True)
    gender = models.CharField(max_length=10, verbose_name="Género", choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')])
    role = models.CharField(max_length=10, verbose_name="Rol de usuario", choices=[('E', 'Entrenador')], default= 'E')
    direccion = models.CharField(max_length= 100, verbose_name = "Direccion",default = 'No posee', null = True, blank = True)
    #comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user)
    

class LugarTrabajo(models.Model):
    NAME_CHOICES = [
        ('AL', 'Aire Libre'),
        ('GY', 'Gimnasio'),
        ('DO', 'Domicilio'),
    ]
    name = models.CharField(
        max_length=2,
        choices=NAME_CHOICES,
        default='AL',
        verbose_name="Tipo de lugar"
    )
    entrenadores = models.ManyToManyField(Entrenador, related_name='Lugares_trabajo')

    def __str__(self):
        return self.get_name_display()

class Equipamiento(models.Model):
    NAME_CHOICES = [
        ('MA', 'Mancuernas'),
        ('BA', 'Barra'),
        ('MQ', 'Maquinas'),
    ]
    name = models.CharField(max_length=3,choices=NAME_CHOICES ,default='N/A' ,verbose_name="Equipamiento disponible")
    entrenadores = models.ManyToManyField(Entrenador, related_name='Equipamiento')

    def __str__(self):
        return self.get_name_display()

class Educacion(models.Model):
    rut_en = models.ForeignKey(Entrenador, on_delete=models.CASCADE,verbose_name = "Rut del entrenador")
    titulo = models.CharField(max_length=40, verbose_name="Titulo")
    nombre_ins = models.CharField(max_length=40, verbose_name="Nombre de la institución")
    ano_egreso = models.IntegerField(verbose_name="Año de egreso", default = 2024)
    
    def __str__(self):
        return str(self.rut_en)

class Disponibilidad(models.Model):
    rut_en = models.ForeignKey(Entrenador, on_delete=models.CASCADE,verbose_name = "Rut del entrenador")
    dia_inicio = models.CharField(max_length=40, verbose_name="Titulo")
    DIA_INICIO_CHOICES = [
        ('LU', 'Lunes'),
        ('MA', 'Martes'),
        ('MI', 'Miercoles'),
        ('JU', 'Jueves'),
        ('VI', 'Viernes'),
        ('SA', 'Sabado'),
        ('DO', 'Domingo'),
    ]
    dia_inicio = models.CharField(max_length=2,choices=DIA_INICIO_CHOICES ,default='LU' ,verbose_name="Dia de inicio de la semana")
    DIA_FIN_CHOICES = [
        ('LU', 'Lunes'),
        ('MA', 'Martes'),
        ('MI', 'Miercoles'),
        ('JU', 'Jueves'),
        ('VI', 'Viernes'),
        ('SA', 'Sabado'),
        ('DO', 'Domingo'),
    ]
    dia_fin = models.CharField(max_length=2,choices=DIA_FIN_CHOICES ,default='LU' ,verbose_name="Dia de inicio de la semana")
    hora_in = models.TimeField()
    hora_fin = models.TimeField()
    
    def __str__(self):
        return str(self.rut_en)
    
class Especializacion(models.Model):
    entrenadores = models.ManyToManyField(Entrenador, related_name='Especializacion')
    ESPECIALIZACION_CHOICES = [
        ('PI', 'Pilates'),
        ('YO', 'Yoga'),
        ('HI', 'Hipertrofia'),
        ('RS', 'Resistencia'),
        ('BP', 'Bajada de peso'),
        ('FU', 'Futbol'),
        ('AT', 'Atletismo'),
        ('PA', 'Pliometria'),
        ('PL', 'Powerlifting'),
    ]
    nombre_esp = models.CharField(max_length=2,choices=ESPECIALIZACION_CHOICES ,default='HI' ,verbose_name="Nombre de especializacion")
    
    def __str__(self):
        return self.get_nombre_esp_display()

class Modalidad(models.Model):
    entrenadores = models.ManyToManyField(Entrenador, related_name='Modalidades')
    MODALIDAD_CHOICES = [
        ('OL', 'Online'),
        ('PR', 'Presencial'),   
    ]
    nombre_modalidad = models.CharField(max_length=2,choices=MODALIDAD_CHOICES ,default='PR' ,verbose_name="Nombre de la Modalidad")
    
    def __str__(self):
        return self.get_nombre_modalidad_display()
    
class Experiencia(models.Model):
    rut_en = models.ForeignKey(Entrenador, on_delete=models.CASCADE,verbose_name = "Rut del entrenador")
    cargo = models.CharField(max_length=40, verbose_name="Cargo del entrenador")
    anos_exp = models.IntegerField(verbose_name="Años de experiencia", default = 1)
    desc = models.TextField(verbose_name= "Descripción de la experiencia")

    def __str__(self):
        return f"{self.rut_en} ({self.anos_exp} años de experiencia)"

class AvatarEntr(models.Model):
    rut_en = models.OneToOneField(Entrenador, on_delete=models.CASCADE, verbose_name = "Rut del entrenador")
    avatar = models.ImageField(upload_to='avatars', verbose_name = "Avatar del entrenador")

class ImgEntr(models.Model):
    rut_en = models.ForeignKey(Entrenador, on_delete=models.CASCADE,verbose_name = "Rut del entrenador")
    img_entr = models.ImageField(upload_to='avatars', verbose_name = "Imagen del entrenador")