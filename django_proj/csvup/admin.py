#from pyexpat import model
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Product

admin.register(Product)

class ProductAdmin(ImportExportModelAdmin):
    list_display = ('id','name', 'sku', 'description')