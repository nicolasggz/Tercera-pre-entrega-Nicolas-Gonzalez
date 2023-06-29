from django import forms

class CrearGatoFormulario(forms.Form):
    nombre=forms.CharField(max_length=20)
    edad=forms.IntegerField()
    fecha_nacimiento=forms.DateField(required=False)
    
class CrearPersonaFormulario(forms.Form):    
    nombre_persona=forms.CharField(max_length=20)
    edad_persona=forms.IntegerField()
    dni=forms.IntegerField()
    
class CrearUbicacionFormulario(forms.Form):
    direccion=forms.CharField(max_length=50)
    pais=forms.CharField(max_length=15)
    codigo_postal=forms.IntegerField()
    
    
    