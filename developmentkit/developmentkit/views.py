from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the Blogs index.")


# dynamic routing
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
