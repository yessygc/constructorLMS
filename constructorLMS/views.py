from django.http import HttpResponse
from django.template import Context, Template

# Request:Para realizar peticiones
# HttpResponse: Para enviar la respuesta usando el protocolo HttpResponse

# Esta es una vista:
def bienvenida(request): # 
    return HttpResponse("Bienvenida o bienvenido a la primera versión del constructor de contenido para un LMS")

def bienvenidaRojo(request): # 
    return HttpResponse("<p style='color: red;'> Bienvenida o bienvenido a la primera versión del constructor de contenido para un LMS</p>")

def miprimeraPlantilla(request):
    # Abrimos el documento que contiene la plantilla:
    plantillaExterna = open("C:/constructorLMS/constructorLMS/plantillas/constructor.html")
    # Se carga el documento en una variable de tipo 'Template':
    template = Template(plantillaExterna.read())
    # Cerramos el documento externo que hemos abierto:
    plantillaExterna.close()
    # Creamos un contexto:
    contexto = Context()
    # Renderizamos el documento:
    documento = template.render(contexto)
    return HttpResponse(documento)