from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def login(request):
    return render(request,'home.html')

def cadastro_usuario(request):
    return render(request, 'cadastro_usuario.html')

def salvar_dados(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'],request.POST['email'] , "request.POST['password']")
        user.first_name = request.POST['name']
        user.save()
        data['msg'] = 'Usuário Cadastrado com Sucesso!'
        data['class'] = 'alert-success'      
    return render(request, 'cadastro_usuario.html', data)