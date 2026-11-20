
from django.http import HttpResponse
from django.urls import path
from . import views

def inicio(request):
    return HttpResponse("Mi proyecto Django funciona correctamente")

urlpatterns = [
    path("", inicio, name="inicio"),
    path("programas/crear/", views.crear_programa, name="crear_programa"),
]
