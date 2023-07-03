import json
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.
def Login(req):
    if req.method== "POST":
        data = json.loads(req.body)
        uname = data["uname"]
        pwd = data["pwd"]

        user = authenticate(username=uname, password=pwd)

        if user is not None:
            login(req,user)
            return HttpResponse("login success")
        else:
            return HttpResponse("login failed", status=401)


def Signup(req):
    if req.method== "POST":
        data = json.loads(req.body)
        fname = data["fname"]
        lname = data["lname"]
        uname = data["uname"]
        pwd = data["pwd"]
        email = data["email"]
        print(req.user.is_authenticated)
        print(req.session.session_key)
        print(req.user)
        
        myuser = User(username=uname,email=email,password=pwd)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        return HttpResponse("signin success")
    else:
        return HttpResponse("signin failed", status=505)

def Logout(req):
    logout(req)
    return HttpResponse("logout success")