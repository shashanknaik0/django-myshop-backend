from django.urls import path
from . import views

urlpatterns = [
    path('', views.productHandler),
    path('delete/<int:id>', views.productDelete),
    path('update/<int:id>',views.productUpdate),
]