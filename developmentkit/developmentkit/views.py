from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    data = {
        'title': 'Home Page',
    }
    return render(request, 'index.html', data)


def blogs(request):
    return HttpResponse("Hello, world. You're at the Blogs.")


# dynamic routing
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
