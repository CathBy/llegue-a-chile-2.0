from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona,Subscripcion,Aviso
from django.shortcuts import redirect
from datetime import datetime

#importar user
from django.contrib.auth.models import User
#sistema de autenticación 
from django.contrib.auth import authenticate,logout, login as auth_login
from django.contrib.auth.decorators import login_required

def index(request):
    usuario = request.session.get('usuario',None)
    return render(request, 'index.html', {'personas':Persona.objects.all(),'usuario':usuario})

def registro(request):
    return render(request,'formulario.html', {})

def avisos(request):
    return render(request,'aviso.html',{})    

def crear(request):
    rut = request.POST.get('rut','')
    correo = request.POST.get('correo','')
    nombre = request.POST.get('nombre','')
    nacimiento = request.POST.get('nacimiento','')
    telefono = request.POST.get('telefono','')
    contrasenia = request.POST.get('contrasenia','')
    persona = Persona(rut=rut,correo=correo,nombre=nombre,nacimiento=str(nacimiento),telefono=telefono,contrasenia=contrasenia)
    print(str(persona))
    persona.save()
    return redirect('index')
   

@login_required(login_url='entrar')
def cerrar_session(request):
    del request.session['usuario']
    logout(request)
    return redirect('index')

def entrar(request):
    return render(request,'index.html',{})   

def entrar_iniciar(request):
    correo = request.POST.get('nombre_usuario','')
    contrasenia = request.POST.get('contrasenia','')
    
    user = authenticate(username=correo, password=contrasenia)

    if user is not None:
        
        request.session['usuario'] = user.first_name+" "+user.last_name
        return redirect("adopcion")
    else:
        return redirect("index")  

def crear_aviso(request):
    titulo = request.POST.get('titulo','')
    emailcontacto = request.POST.get('emailcontacto','')
    contacto = request.POST.get('contacto','')
    descripcion = request.POST.get('descripcion','')
    aviso=Aviso(titulo=titulo,emailContacto=emailcontacto,contacto=contacto,descripcion=descripcion)
    print(str(aviso))
    aviso.save()
    return redirect('aviso')
