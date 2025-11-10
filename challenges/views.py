from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    "january":"January Eat no meal for 30 days",
    "february":"February walk for atleast 20 minutes a day!",
    "march":"march Eat no meal for 30 days",
    "april":"april walk for atleast 20 minutes a day!",
    "may":"may Eat no meal for 30 days",
    "june":"june walk for atleast 20 minutes a day!",
    "july":"july Eat no meal for 30 days",
    "augast":"augast walk for atleast 20 minutes a day!",
    "september":"september Eat no meal for 30 days",
    "october":"october walk for atleast 20 minutes a day!",
    "november":"november Eat no meal for 30 days",
    "december":"december walk for atleast 20 minutes a day!",
}

# FOR FIXED ROUTING
# def january(request):
#     return HttpResponse("Eat no meal for 30 days")

# def february(request):
#     return HttpResponse("walk for atleast 20 minutes a day!")

# def march(request):
#     return HttpResponse("This is march challenge")

# FOR DYNAMIC ROUTING
def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())
        if month > len(months):
            return HttpResponseNotFound("Invalid month name or number")
        redirect_month = months[month - 1]

        # dynamic reverse path redirection using path name
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("Please enter values from o to 12")

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported")    
