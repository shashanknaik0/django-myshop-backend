from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.Signup),
    path('login',views.Login),
    path('logout',views.Logout),
]