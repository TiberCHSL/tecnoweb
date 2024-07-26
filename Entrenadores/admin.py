from django.contrib import admin

# Register your models here.
from .models import Cliente, Entrenador, LugarTrabajo, Equipamiento, Educacion, Disponibilidad, Especializacion, Modalidad, Experiencia, ImgEntr, AvatarEntr
admin.site.register(Cliente)
admin.site.register(Entrenador)
admin.site.register(LugarTrabajo)
admin.site.register(Equipamiento)
admin.site.register(Educacion)
admin.site.register(Disponibilidad)
admin.site.register(Especializacion)
admin.site.register(Modalidad)
admin.site.register(Experiencia)
admin.site.register(ImgEntr)
admin.site.register(AvatarEntr)
