
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name = "home"),
    path("cadastro_usuario/",views.cadastro_usuario, name='cadastro_usuario'),
    path("salvar_dados/",views.salvar_dados, name='salvar_dados'),
    path("tela_login/",views.tela_login, name='tela_login'),
    path("process_login/",views.process_login, name='process_login'),
    path("dashboard/", views.dashboard, name='dashboard'),
    path("logouts/", views.logouts, name='logouts'),
    path("password/", views.changePassowrd, name='password'),

   
]