from django import forms
from .models import Product

class ProductData(forms.Form):
	class meta:
		model = Product
		fields = '__all__'