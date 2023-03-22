from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenge_dict = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None,
}


# monthly challenge dynamic url
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenge_dict[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")


def monthly_challenge_by_month(request, month):
    months = list(monthly_challenge_dict.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]

    return HttpResponseRedirect("/challenges/" + redirect_month)
