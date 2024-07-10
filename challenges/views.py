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
    "december": "Walk for at least 1000 steps every day.",
}


def index(request):
    month_list = ""
    list_header = "<h1>Monthly Challenges</h1>"
    for month in all_challenges:
        month_path = reverse("month-challenge", args=[month])
        month_list += f"<li><a href='{month_path}'>{month.title()}</a></li>"
    return HttpResponse(list_header + f"<ul>{month_list}</ul>")


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
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This is not a valid month.</h1>")
