
from django.urls import path
from . import views

urlpatterns = [
    path("",views.login, name = "login"),
    path("cadastro_usuario/",views.cadastro_usuario, name="cadastro_usuario"),
    path("salvar_dados/",views.salvar_dados, name="salvar_dados"),

   
]