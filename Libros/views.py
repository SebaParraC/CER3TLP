from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro
from django.views.generic import DetailView

# Create your views here.

def index(request):

    libros = Libro.objects.all()
    libros = libros.filter(disponible=True)
    oferta = False
    for libro in libros:
        if libro.descuento != 0:
            oferta = True
            descuento = libro.precio -((libro.precio * libro.descuento ) / 100)
            libro.descuentoCalculado = descuento
    data = {
        'libros':libros,
        'oferta':oferta
    }
    return render(request,'Libros/index.html',data)

class detalleLibro(DetailView):
    model = Libro
    template_name = 'Libros/detalle_libro.html'
    context_object_name= 'libro'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        libro = self.object
        if libro.descuento != 0:
            descuento = libro.precio -((libro.precio * libro.descuento)/100)
            context['descuento'] = descuento
        else:
            context['descuento'] = 0
        return context