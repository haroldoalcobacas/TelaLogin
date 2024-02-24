

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request,'home.html')

def cadastro_usuario(request):
    return render(request, 'cadastro_usuario.html')

def salvar_dados(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger' 
    else:
        user = User.objects.create_user(request.POST['user'],request.POST['email'] , request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        data['msg'] = 'Usuário Cadastrado com Sucesso!'
        data['class'] = 'alert-success'      
    return render(request, 'cadastro_usuario.html',data)


def dashboard(request):
    return render(request,'dashboard/home.html')

def tela_login(request):
    return render(request,'tela_login.html')

def process_login(request):   
        
        user = authenticate(username=request.POST['user'], password=request.POST['password'])
        data = {}
        if user is not None:           
            login(request, user)
            return redirect('/dashboard/')
            
        else:
            data['msg'] = 'Usuário ou Senha Incorretas!'
            data['css'] = 'alert-danger' 
            return render(request,'tela_login.html',data)
    
    
def logouts(request):
    logout(request)
    return redirect('/tela_login/')

def changePassowrd(request):
    user = User.objects.get(email=request.user.email)
    user.set_password(request.POST['password'])
    user.save()
    logout(request)
    return redirect('/tela_login/')