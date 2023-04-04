from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    data = {
        'title': 'Home Page',
        'values': ['php', 'python', 'java', 'c++'],
        'students': [
            {'name': 'John', 'age': 18},
            {'name': 'Bob', 'age': 20},
            {'name': 'Alice', 'age': 19},
            {'name': 'Kate', 'age': 21},
        ]
    }
    return render(request, 'index.html', data)


def blogs(request):
    return HttpResponse("Hello, world. You're at the Blogs.")


# dynamic routing
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
