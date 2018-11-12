from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona,Suscripcion,Aviso
from django.shortcuts import redirect
from datetime import datetime

#importar user
from django.contrib.auth.models import User
#sistema de autenticación 
from django.contrib.auth import authenticate,logout, login as auth_login
from django.contrib.auth.decorators import login_required

def index(request):
    usuario = request.session.get('usuario',None)
    return render(request, 'index.html', {'personas':Persona.objects.all(),'usuario':usuario,'aviso':Aviso.objects.all(),'usuario':usuario})

def registro(request):
    return render(request,'formulario.html', {})

def avisos(request):
    return render(request,'aviso.html',{})    

def trabajo(request):
    return render(request,'trabajo.html',{})

def transporte(request):
    return render(request,'transporte.html',{})

def conocer(request):
    return render(request,'conocer.html',{})
def documentacion(request):
    return render(request,'documentacion.html',{})    
def educacion(request):
    return render(request,'educacion.html',{})
def salud(request):
    return render(request,'salud.html',{})    
def vivienda(request):
    return render(request,'vivienda.html',{})    
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
    aviso=Aviso(titulo=titulo,emailcontacto=emailcontacto,contacto=contacto,descripcion=descripcion)
    print(str(aviso))
    aviso.save()
    return redirect('avisos')



