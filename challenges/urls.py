from django.urls import path
from . import views

urlpatterns = [
    # FIXED ROUTING
    # path("january", views.january),
    # path("february", views.february),
    # path("march", views.march),

    # DYNAMIC ROUTING
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge") # name is given to make it dynamic path
]