import pandas as pd
from django.shortcuts import render
from .resources import ProductResource
from tablib import Dataset
from .models import Product

"""def export(request):
    prod_resource = ProductResource()
    dataset = prod_resource.export()
    response = HttpResponse(dataset.csv, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="test.csv"'
    return response"""

def simple_upload(request):
    if request.method == 'POST':
        prod_resource = ProductResource()
        dataset = Dataset()
        new_products = request.FILES['myFile']

        imported_data = dataset.load(new_products.read().decode('utf-8'),format='csv')
        #print(imported_data)
        #imported_data = imported_data.remove_duplicates(['SKU'])

        for data in imported_data:
            #print(data[2])
            value = Product(data[0],data[1],data[2],data[3])
            value.save()       
    return render(request, 'upload.html')

