import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Cart,Product

# Create your views here.
@login_required
def cart(request):
    if request.method == "GET":
        userId = request.user.id
        items = Cart.objects.select_related("product_id").filter(user_id = userId)
        result = []
        for x in items:
            result.append({"id":x.id,"name":x.product_id.name,"price":x.product_id.price, "quantity":x.product_id.quantity, "imgURL":x.product_id.imgURL, "description":x.product_id.description})

        return JsonResponse(result,safe=False)
    
    elif request.method == "POST":
        data = json.loads(request.body)
        productId = data["productId"]
        userId = request.user

        product = Product.objects.get(id=productId)

        cartItem = Cart(user_id = userId ,product_id=product)
        cartItem.save()
        return HttpResponse("saved cart")

@login_required
def deleteCart(request, id):
    if request.method == "DELETE":
        userId = request.user.id
        print(id)
        item = Cart.objects.filter(id=id, user_id=userId)
        if item:
            item.delete()
            return HttpResponse("item deleted")
        else:
            return HttpResponse("item not exists")