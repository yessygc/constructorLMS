import datetime
from django.http import HttpResponse
from django.template import Context, Template
# from django.template import loader
from django.template.loader import get_template
from django.shortcuts import render
# Request:Para realizar peticiones
# HttpResponse: Para enviar la respuesta usando el protocolo HttpResponse

# Esta es una vista:
def bienvenida(request): # 
    return HttpResponse("Bienvenida o bienvenido a la primera versión del constructor de contenido para un LMS")

def bienvenidaRojo(request): # 
    return HttpResponse("<p style='color: red;'> Bienvenida o bienvenido a la primera versión del constructor de contenido para un LMS</p>")

def miprimeraPlantilla(request):
    # Abrimos el documento que contiene la plantilla:
    plantillaExterna = open("C:/constructorLMS/constructorLMS/plantillas/plantillaEjemplos.html")
    # Se carga el documento en una variable de tipo 'Template':
    template = Template(plantillaExterna.read())
    # Cerramos el documento externo que hemos abierto:
    plantillaExterna.close()
    # Creamos un contexto:
    contexto = Context()
    # Renderizamos el documento:
    documento = template.render(contexto)
    return HttpResponse(documento)

def plantillaParametros(request):
    nombre = "Yessyca"
    fechaActual = datetime.datetime.now()
    lenguajes = ["Python", "Ruby", "JavaScript", "Java", "PHP", "C#", "Kotlin"]
    # Abrimos el documento que contiene la plantilla:
    plantillaExterna = open("C:/constructorLMS/constructorLMS/plantillas/plantillaEjemplos.html")
    # Se carga el documento en una variable de tipo 'Template':
    template = Template(plantillaExterna.read())
    # Cerramos el documento externo que hemos abierto:
    plantillaExterna.close()
    # Creamos un contexto:
    contexto = Context({"nombrePersona": nombre, "fechaActual": fechaActual, "lenguajes": lenguajes})
    # Renderizamos el documento:
    documento = template.render(contexto)
    return HttpResponse(documento)

def plantillaCargador(request):
    nombre = "Yessyca"
    fechaActual = datetime.datetime.now()
    lenguajes = ["Python", "Ruby", "JavaScript", "Java", "PHP", "C#", "Kotlin"]
    # Estamos especificando donde se encuentran las plantillas y creamos una variable que la almacena
    plantillaExterna = get_template('plantillaEjemplos.html')
    # Renderizar el documento
    documento = plantillaExterna.render({"nombrePersona": nombre, "fechaActual": fechaActual, "lenguajes": lenguajes})
    return HttpResponse(documento)

def plantillaShortcut(request):
    nombre = "Yessyca"
    fechaActual = datetime.datetime.now()
    lenguajes = ["Python", "Ruby", "JavaScript", "C++" "Java", "PHP", "C#", "Kotlin"]

    return render(request,'plantillaEjemplos.html', {"nombrePersona": nombre, "fechaActual": fechaActual, "lenguajes": lenguajes} )


def constructor(request):
    return render(request, 'constructor.html', {})

def plantillaNavegacion(request):
    return render(request, 'plantillaNavegacion.html', {})

def plantillaMinimizado(request):
    return render(request, 'plantillaMinimizado.html', {})

def plantillaComponentes(request):
    return render(request, 'plantillaComponentes.html', {})
