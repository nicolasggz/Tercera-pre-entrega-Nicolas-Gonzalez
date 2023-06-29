from django.shortcuts import render
from inicio.forms import CrearGatoFormulario
from inicio.forms import CrearPersonaFormulario
from inicio.forms import CrearUbicacionFormulario
from inicio.models import Gato
from inicio.models import persona_responsable
from inicio.models import ubicacion

# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')
    

def crear_gato(request):
    mensaje = ''
    
    if request.method == 'POST':
        formulario = CrearGatoFormulario(request.POST)
        formulario2 = CrearPersonaFormulario(request.POST)
        formulario3 = CrearUbicacionFormulario(request.POST)
        if formulario.is_valid() and formulario2.is_valid() and formulario3.is_valid():
            info = formulario.cleaned_data
            info2 = formulario2.cleaned_data
            info3 = formulario3.cleaned_data
            gato = Gato(nombre=info['nombre'],edad=info['edad'],fecha_nacimiento=info['fecha_nacimiento'])
            persona = persona_responsable(nombre_persona=info2['nombre_persona'],edad_persona=info2['edad_persona'],dni=info2['dni'])
            ubicacion_persona = ubicacion(direccion=info3['direccion'],pais=info3['pais'],codigo_postal=info3['codigo_postal'])

            gato.save()
            persona.save()
            ubicacion_persona.save
            mensaje = f'Se creo el gato {gato.nombre}'
            return render(request, 'inicio/crear_gato.html', {'formulario': formulario,'formulario2': formulario2,'formulario3': formulario3})
        else:
            return render(request, 'inicio/crear_gato.html', {'formulario': formulario,'formulario2': formulario2,'formulario3': formulario3})
    
    formulario=CrearGatoFormulario()
    formulario2=CrearPersonaFormulario()
    formulario3=CrearUbicacionFormulario()
    return render(request, 'inicio/crear_gato.html',{'formulario': formulario,'formulario2': formulario2,'formulario3': formulario3, 'mensaje':mensaje})
