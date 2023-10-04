from django import forms

from matery.models import matery

class FormMatery(forms.ModelForm):

	class Meta:
		model = matery

		fields = [
			'user',
			'Matematicas1',
			'Matematicas2',
			'Matematicas3',
			'Matematicas4',
			'Matematicas5',
			'Matematicas6',
			'Matematicas7',
			'Matematicas8',
			'Matematicas9',
			'Matematicas10',
			
		]
		labels = {
			'user': 'Seleccione su usuario',
			'Matematicas1': '¿Que son los números naturales?',
			'Matematicas2': '¿Que son los números enteros?',
			'Matematicas3': '√432',
			'Matematicas4': '2918838/897',
			'Matematicas5': '(45/26)*(39/25)*(22/33)',
			'Matematicas6': '6. x-(2x+1)=8-(3x+3)',
			'Matematicas7': '7. (5-3x)-(-4x+6)=(8x+11)-(3x-6)',
			'Matematicas8': '8. La suma de 2 numeros es 9 y la suma de sus cuadrados 53 hallar los números',
			'Matematicas9': '9. A tiene 3 años mas que B y el cuadrado de la edad de A aumentada en el cuadrado de la edad de B equivale a 317 años Hallar ambbas edades ',
			'Matematicas10': '10. Un vaso tiene agua se coloca un objeto y la altura sube 10 cm si el radio del vaso es de 5 cm ¿Cual es el volumen del objeto?',			
			
		}
		widgets = {
			'Matematicas1': forms.TextInput(attrs={'class':'form-control'}),
			'Matematicas2': forms.TextInput(attrs={'class':'form-control'}),
			'Matematicas3': forms.TextInput(attrs={'class':'form-control'}),
			'Matematicas4': forms.TextInput(attrs={'class':'form-control'}),
			'Matematicas5': forms.TextInput(attrs={'class':'form-control'}),
			'Matematicas6': forms.TextInput(attrs={'class':'form-control'}),
			'Matematicas7': forms.TextInput(attrs={'class':'form-control'}),
			'Matematicas8': forms.TextInput(attrs={'class':'form-control'}),
			'Matematicas9': forms.TextInput(attrs={'class':'form-control'}),
			'Matematicas10': forms.TextInput(attrs={'class':'form-control'}),
		}