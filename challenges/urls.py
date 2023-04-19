from django.urls import path
from . import views

urlpatterns = [

    # path ("January", views.January),
    # path("february",views.February),
    # path("March",views.March),
    # buit in placeholder syntax
    # helper transformation <str:..>or int
    path("",views.index, name="index"),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>",views.monthly_challenges, name= "month-challenge")
]

