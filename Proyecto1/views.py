from django.http import HttpResponse
import datetime
from django.template import Template,Context,loader
from django.shortcuts import render

class Persona (object):
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo (request): #funcion denominada como vista o primera vista y hay que enlazar a una url

    p1=Persona("profesor Holger","CORNEJO")

    #nombre="Daniel"

    #apellido="Cornejo"

    temasDelCurso=["plantillas","Modelos","formularios","vistas","despliegue"]

    ahorita = datetime.datetime.now()
    #esto ya no se hace
    #documento_externo=open("/Users/daniel/NetBeansProjects/ProyectosDjango/Proyecto1/Proyecto1/plantillas/miplantilla.html")

    #plantilla=Template(documento_externo.read())

    #documento_externo.close()

    #documento_externo=loader.get_template('miplantilla.html')
    nombres = {"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahorita, "temas":temasDelCurso}
    #contexto=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahorita, "temas":temasDelCurso}) #al context se le manda como parametros de llave:valor los argumentos

    #documento=documento_externo.render({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahorita, "temas":temasDelCurso})

    return render(request,"miplantilla.html",nombres)#HttpResponse(documento)

def despedida (request):
    return HttpResponse("hasta luego, esta es una despedida hecha en una funcion")


def fecha(request):

    fecha_actual = datetime.datetime.now()

    documento = """
    <html>
        <body>
            <h3>
            Fecha y Hora actuales %s
            </h3>
        </body>
    </html>
    """ % fecha_actual

    return HttpResponse(documento)


def calculaEdad (request,edad,anio):
    edadActual=edad
    periodo=anio-2019
    edadFutura=edadActual+periodo
    documento="""
    <html>
        <body>
            <h4>
            En el año %s tendrás %s años
            </h4>
        </body>
    </html>
    """ %(anio, edadFutura)

    return HttpResponse(documento)

def cursoC(request):
    ahoritaYA = datetime.datetime.now()
    return render(request,"CursoC.html",{"fecha":ahoritaYA})

def cursoCSS(request):
    ahoritaYA = datetime.datetime.now()
    return render(request,"cursoCSS.html",{"fecha":ahoritaYA})

