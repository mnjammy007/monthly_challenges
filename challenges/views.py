from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

all_challenges = {
    "january": "Eat no meat for the entire month of January.",
    "february": "Walk for at least 1000 steps every day.",
    "march": "Walk for at least 1000 steps every day.",
    "april": "Eat no meat for the entire month.",
    "may": "Walk for at least 1000 steps every day.",
    "june": "Walk for at least 1000 steps every day.",
    "july": "Eat no meat for the entire month.",
    "august": "Walk for at least 1000 steps every day.",
    "september": "Walk for at least 1000 steps every day.",
    "october": "Eat no meat for the entire month.",
    "november": "Walk for at least 1000 steps every day.",
    "december": None,
}


def index(request):
    return render(request, "challenges/index.html", {"months": all_challenges.keys()})


def monthly_challenge_by_number(request, month):
    try:
        forward_month = list(all_challenges.keys())[month - 1]
        redirect_path = reverse("month-challenge", args=[forward_month])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("<h1>This is not a valid month.</h1>")


def monthly_challenge(request, month):
    try:
        challenge_text = all_challenges[month]
        return render(
            request,
            "challenges/challenge.html",
            {"month": month, "text": challenge_text},
        )
    except:
        return HttpResponseNotFound("<h1>This is not a valid month.</h1>")
