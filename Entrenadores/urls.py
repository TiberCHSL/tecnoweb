from django.urls import path
from .views import custom_logout, custom_login, add_modalidades, add_lugares_trabajo, add_equipamientos, add_especializaciones, entrenadores_view, clientes_view, add_educacion, add_experiencia
from .views import TrainerListView, trainer_detail
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    #path("", views.index, name="index"),
    path('register/', views.registration_selection, name='registration_selection'),
    path('register/cliente/', views.register_cliente, name='register_cliente'),
    path('register/entrenador/', views.register_entrenador, name='register_entrenador'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('add-modalidades/', add_modalidades, name='add_modalidades'),
    path('add-lugares-trabajo/', add_lugares_trabajo, name='add_lugares_trabajo'),
    path('add-equipamientos/', add_equipamientos, name='add_equipamientos'),
    path('add-especializaciones/', add_especializaciones, name='add_especializaciones'),
    path('entrenadores/', entrenadores_view, name='entrenadores_view'),
    path('clientes/',clientes_view, name='clientes_view'),
    path('add_educacion/', add_educacion, name='add_educacion'),
    path('add_experiencia/', add_experiencia, name='add_experiencia'),
    path('trainers/', TrainerListView.as_view(), name='trainer_list'),
    path('trainer/<str:trainer_rut>/', trainer_detail, name='trainer_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)