from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

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
    # "december":"december walk for atleast 20 minutes a day!",
    "december": None,
}

# FOR FIXED ROUTING
# def january(request):
#     return HttpResponse("Eat no meal for 30 days")

# def february(request):
#     return HttpResponse("walk for atleast 20 minutes a day!")

# def march(request):
#     return HttpResponse("This is march challenge")

def index(request):
    try:
        months = list(monthly_challenges.keys())
        html_markup = ""
        for month in months:
            month_path = reverse("month-challenge", args=[month])
            html_markup += f"""
                <li><a href={month_path}>{month}</a></li>
            """
        response_data = f"<ul>{html_markup}</ul>"

        return render(request, "challenges/index.html",{
            "path":month_path,
            "months": months
        })
    
    except:
        return HttpResponseNotFound("Not found")

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

        # METHOD 1: using render_to_string
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)

        # METHOD 1: using render
        return render(request,"challenges/challenge.html", {
            
            "month":month,
            "text":challenge_text
        })
    except:
        raise Http404()
        # response_date = render_to_string("404.html")
        # return HttpResponseNotFound(response_date)    
