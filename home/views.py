# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

from .models import Niveles, Usuario, Entrenado

from PIL import Image

from datetime import date, datetime

def now_training(request):
    if request.method == "POST":
        today = date.today()
        topics = Usuario.objects.get(nombres = request.POST["nombres"], apellidos = request.POST["apellidos"])
        change = Entrenado.objects.get(id = topics.id)
        change.entrenado = 1
        change.save(update_fields=['entrenado'])
        return render(request,"list_user.html")
        

def training(request):
    return render(request,"training.html")

def update_training(request):
    data = list(Entrenado.objects.values())
    users = list(Usuario.objects.values())
    list_users = []
    today = date.today()
    for d in data:
        if d['entrenado'] == False and today == datetime.date(d['fecha']):
            for u in users:
                if u['id'] == d['id']:
                    list_users.append(u)

    return JsonResponse(list_users, safe=False)
            

def list_user(request):
    return render(request,"list_user.html")

def test_ag(request):
    data = list(Niveles.objects.values())
    return JsonResponse(data, safe=False)
    

def get_topics_ajax(request):
    if request.method == "POST":
        try:
            topics = Niveles.objects.all()

        except Exception:
            return JsonResponse({'error_message': 'error'})
        return JsonResponse(list(topics.values('id', 'nivel')), safe = False) 

def wizard_register_trainer(request):
    return render(request,"wizard_register_trainer.html")

def new_day(request):
    users = list(Usuario.objects.values())
    today = date.today()

    try:
        topics = Entrenado.objects.get(fecha = today)
        return render(request,"page-500.html")
    except:
        for i in users:
            b = Entrenado(
            id = i['id'],
            fecha = today,
            entrenado = False)
            b.save()


    return render(request,"index.html")

def profile(request):
    if request.method=='POST':
        b = Usuario(
        nombre_usuario = request.POST["user_name"],
        nombres = request.POST["name"],
        apellidos = request.POST["last_name"],
        nivel = request.POST["nivel"],
        dni = request.POST["number_dni"],
        peso = request.POST["peso"],
        altura = request.POST["altura"],
        correo = request.POST["email"],
        direccion = request.POST["direction"],
        descripcion = request.POST["description"],
        image = request.FILES["img_avatar"]        )
        b.save()
        return render(request,"index.html")
    return render(request,"profile.html")

def show_img(request):
    imagePath = 'static/assets/img/img.jpg'
    response = HttpResponse(content_type ="image/png")
    img = Image.open(imagePath)
    img.save(response,'png')
    return response

def level(request):
    print("HI")
    if request.method=='POST':
        level_name = request.POST["level_name"]
        b = Niveles(nivel=level_name)
        b.save()
        return render(request,"index.html")

    return render(request,"level.html")

def register_trainers(request):
    if request.method=='POST':
        name = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        
        body = "Su usuario es: " + name + "\nSu contraseña es:" + password

        email_from= settings.EMAIL_HOST_USER
        
        recipient_list=[email]
        
        send_mail("Registro",body,email_from,recipient_list)
        
        return render(request,"index.html")

    return render(request,"register.html")

def register_user(request):
    if request.method=='POST':
        name = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        
        body = "Su usuario es: " + name + "\nSu contraseña es:" + password

        email_from= settings.EMAIL_HOST_USER
        
        recipient_list=[email]
        
        send_mail("Registro",body,email_from,recipient_list)
        
        return render(request,"index.html")

    return render(request,"register.html")


#@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


#@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
