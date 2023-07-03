from django.http import HttpResponse
from django.middleware.csrf import get_token

def csrf(request):
    return HttpResponse(get_token(request))
