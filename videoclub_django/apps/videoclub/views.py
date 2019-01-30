from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView, UpdateView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from apps.videoclub.forms import *

from apps.videoclub.models import Pelicula, Director, Actor

# Mis decoradores

staff = [
    login_required,
    staff_member_required(login_url='forbidden')
]

class VideoclubIndex(TemplateView):
    template_name = "videoclub/index.html"

    def peliculas(self):
        return Pelicula.objects.all().order_by('-id')[:6]

    def directores(self):
        return Director.objects.all().order_by('-id')[:6]

    def actores(self):
        return Actor.objects.all().order_by('-id')[:6]

class PeliculaDetailView(DetailView):
    model = Pelicula
    template_name = "videoclub/pelicula.html"

class DirectorDetailView(DetailView):
    model = Director
    template_name = "videoclub/director.html"

class ActorDetailView(DetailView):
    model = Actor
    template_name = "videoclub/actor.html"

class PeliculasList(ListView):
    model = Pelicula
    template_name = "videoclub/peliculas.html"

class DirectoresList(ListView):
    model = Director
    template_name = "videoclub/directores.html"

class ActoresList(ListView):
    model = Actor
    template_name = "videoclub/actores.html"

class Forbidden(TemplateView):
    template_name = "videoclub/forbidden.html"

class PeliculasManage(ListView):
    model = Pelicula
    template_name = "videoclub/peliculas_manage.html"

    @method_decorator(staff)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class PeliculasEdit(UpdateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = "videoclub/peliculas_edit.html"
    success_url = reverse_lazy('peliculas_manage')
