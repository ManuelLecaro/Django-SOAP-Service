from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from spyne.application import Application
from spyne.decorator import rpc
from spyne.model.primitive import Unicode, Integer
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from spyne.service import ServiceBase
from .models import TipoPlan
from spyne.model.complex import ComplexModel
from spyne import Integer64

class Bndbox(ComplexModel):
    nombre = ""
    costo = Integer64

    def __init__(self, nombre, costo):
        # don't forget to call parent class initializer
        super(BndBox, self).__init__()

        self.nombre = nombre
        self.costo = costo

class SoapService(ServiceBase):
    @rpc(_returns=(Unicode))
    def tomarplanes(ctx):
        planes = TipoPlan.objects.all()
        listaObjetos = []
        for plan in planes:
            print(str(plan.nombre)+":"+str(plan.costo))
            listaObjetos.append(str(plan.nombre)+":"+str(plan.costo))
        return ', '.join(listaObjetos)


soap_app = Application(
    [SoapService],
    tns='django.soap.requisitos',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

django_soap_application = DjangoApplication(soap_app)
my_soap_application = csrf_exempt(django_soap_application)



# Create your views here.
