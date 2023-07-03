import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Product
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
@login_required
def productHandler(request):
    if request.method == "GET":
        products = Product.objects.all()
        products = serialize("json",products)
        return HttpResponse(products)
    
    elif request.user.is_staff and request.method == "POST":
        data = json.loads(request.body)
        name = data["name"]
        quantity = data["quantity"]
        price = data["price"]
        description = data["description"]
        imgURL = data["imgURL"]

        newProduct = Product(name=name,quantity=quantity,price=price,description=description,imgURL=imgURL)

        newProduct.save()

        return HttpResponse("saved")

@staff_member_required
def productDelete(request, id):
    if request.method == "POST":
        product = Product.objects.get(id=id)

        if product:
            product.delete()
            return HttpResponse("deleted")
        else:
            return HttpResponse("product not exist")
    
@staff_member_required
def productUpdate(request, id):
    if request.method == "POST":
        product = Product.objects.get(id=id)

        if product:
            data = json.loads(request.body)
            name = data["name"]
            quantity = data["quantity"]
            price = data["price"]
            description = data["description"]
            imgURL = data["imgURL"]

            updateProduct = Product(name=name,quantity=quantity,price=price,description=description,imgURL=imgURL)

            updateProduct.save()
            return HttpResponse("updated")
        else:
            return HttpResponse("product not exist")