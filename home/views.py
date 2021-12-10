# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django import urls
from django.contrib.auth.decorators import login_required
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, resolve_url
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView
from django.views.generic.base import View
from .forms import UsuarioSignUpForm
from .models import User
from django.views.generic import CreateView, ListView, View, UpdateView
import json


class LoginUser(LoginView):
    template_name = "login.html"
    def get_success_url(self):
        url = self.get_redirect_url()
        return url or resolve_url("/home/index")

class RegisterUser(CreateView):
    model = User
    form_class = UsuarioSignUpForm
    template_name = "register_user.html"
    success_url = "/home/list_user/"

class UserDelete(View):
    http_method_names = ['get', 'post', 'head', 'options']

    def post(self, request, *args, **kwargs):
        post_data = json.loads(request.body.decode("utf-8"))
        pk = post_data['pk']
        if pk:
            user = User.objects.filter(id=pk)
            user.delete()
        return JsonResponse({'msg': 'OK'})

class UserUpdate(UpdateView):
  model = User
  fields = ('__all__')
  template_name = "update-view.html"
  success_url = '/'


class ListUser(ListView):
  model = User
  template_name = "list_user.html"



from .models import Niveles, Usuario, Entrenado

from PIL import Image

from datetime import date, datetime

def page_user(request):
    return render(request,"page-user.html")


@login_required(login_url="/login/")
def now_training(request):
    if request.method == "POST":
        today = date.today()
        topics = Usuario.objects.get(nombres = request.POST["nombres"], apellidos = request.POST["apellidos"])
        change = Entrenado.objects.get(id = topics.id)
        change.entrenado = 1
        change.save(update_fields=['entrenado'])
        return render(request,"list_user.html")
        
def page_403(request):
    return render(request,"page-403.html")

def page_404(request):
    return render(request,"page-404.html")

def page_500(request):
    return render(request,"page-500.html")

@login_required(login_url="/login/")
def training(request):
    return render(request,"training.html")


@login_required(login_url="/login/")
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
            
@login_required(login_url="/login/")
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

@login_required(login_url="/login/")
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


@login_required(login_url="/login/")
def show_img(request):
    imagePath = 'static/assets/img/img.jpg'
    response = HttpResponse(content_type ="image/png")
    img = Image.open(imagePath)
    img.save(response,'png')
    return response

@login_required(login_url="/login/")
def level(request):
    if request.method=='POST':
        level_name = request.POST["level_name"]
        description = "Esto es el nivel que posees"
        b = Niveles(name_nivel=level_name,description = description)
        b.save()
        return render(request,"index.html")

    return render(request,"level.html")

@login_required(login_url="/login/")
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

@login_required(login_url="/login/")
def comends(request):
    if request.method=='POST':
        palabra_clave = request.POST["palabra_clave"]
        email_contacto = request.POST["email_contacto"]
        comentario = request.POST["comentario"]
        
        body = "Su palabra clave es: " + palabra_clave + "\nEl correo de contacto es:" + email_contacto+ "\nEl comentario es:" + comentario

        email_from= settings.EMAIL_HOST_USER

        email = "kaiser4900@gmail.com"
        
        recipient_list=[email]
        
        send_mail("Registro",body,email_from,recipient_list)
        
        return render(request,"index.html")

    return render(request,"comends.html")


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
