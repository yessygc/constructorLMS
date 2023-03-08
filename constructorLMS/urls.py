"""constructorLMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from constructorLMS.views import bienvenida
from constructorLMS.views import bienvenidaRojo
from constructorLMS.views import miprimeraPlantilla
from constructorLMS.views import plantillaCargador
from constructorLMS.views import plantillaShortcut
from constructorLMS.views import constructor
from constructorLMS.views import plantillaNavegacion
from constructorLMS.views import plantillaMinimizado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenida/', bienvenida),
    path('bienvenida123/', bienvenidaRojo),
    path('plantilla/', miprimeraPlantilla),
    path('plantillaCargador/', plantillaCargador),
    path('plantillaShortcut/', plantillaShortcut),
    path('constructor/', constructor),
    path('navegacion/', plantillaNavegacion),
    path('minimizado/', plantillaMinimizado)
]
