from django.urls import path
from . import views

urlpatterns = [
    path('',views.cart),
    path('<int:id>',views.deleteCart),
]
