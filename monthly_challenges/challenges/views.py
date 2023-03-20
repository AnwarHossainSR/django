from django.http import HttpResponse

# Create your views here.


def january(request):
    return HttpResponse("This is the monthly challenge for January")


def february(request):
    return HttpResponse("This is the monthly challenge for February")
