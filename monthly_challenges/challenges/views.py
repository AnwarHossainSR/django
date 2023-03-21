from django.http import HttpResponse

# Create your views here.

# def january(request):
#     return HttpResponse("This is the monthly challenge for January")

# def february(request):
#     return HttpResponse("This is the monthly challenge for February")


# monthly challenge dynamic url
def monthly_challenge(request, month):
    challenge_text = None

    # set different challenge for different month
    if month == "january":
        challenge_text = "Eat no meat for the entire month!"
    elif month == "february":
        challenge_text = "Walk for at least 20 minutes every day!"
    elif month == "march":
        challenge_text = "Learn Django for at least 20 minutes every day!"
    elif month == "april":
        challenge_text = "Eat no meat for the entire month!"
    else:
        return HttpResponse("This month is not supported")

    return HttpResponse(challenge_text)
