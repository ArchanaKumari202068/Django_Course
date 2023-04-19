from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string



# Create your views here.
# def January(request ):
#     return HttpResponse("Eat no meal for entire month")
# def February(request):
#     return HttpResponse("walk for atleat 20 min every day")
# def March(request):
#     return HttpResponse("Learn every day React atleast 20 min")





# adding more dynamic  view logic 

monthly_challenge ={
    "january":"Eat no meal for the entire month",
    "february": "walk for at least 20 minutes every day",
    "march": "Learn every day django atleast  20 min",
    "april": "hello",
    "may":"learn mongodb",
    "june":"Eat no meal for the entire month",
    "july": "walk for at least 20 minutes every day",
    "August": "Learn every day django atleast  20 min",
    "Sep":' This month is not supported',
    "Oct": " This month is not supported",
    "Nov": "  This month is not supported",
    "Dec": "  This month is not supported",


}

def index(request):
    
    months =list(monthly_challenge.keys())

    return render(request,"challenges/index.html", {
        "months":months
    })

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge",args = [month])
    #     list_items += f"<li><a href= \"{month_path}\">{capitalized_month}</a></li>"



    # response_data = f"<ul>{list_items}</ul>" 
    # return HttpResponse(response_data)


# Redirect 

# Dynamic path segments and Captured

def monthly_challenge_by_number(request,month):
    months= list(monthly_challenge.keys())

    if month > len(months):
       return HttpResponseNotFound("Invalid Month") 
    
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge",args=[redirect_month]) # /challenge/january
    # return HttpResponseRedirect("/challenge/" + redirect_month)
    return HttpResponseRedirect(redirect_path)




def monthly_challenges(request,month):
    try: 
        challenge_text = monthly_challenge[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name":  month.capitalize()
        })
        # response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data )

    except:
        return render(request,"404.html")
        response_data =  render_to_string("404.html")
        # return HttpResponseNotFound(" This month is not supported")   


    # if month =="january":
    #     challenge_text = "Eat no meal for the entire month"
    # elif month=="february":
    #     challenge_text = "walk for at least 20 minutes every day"    
    # elif month=="march":
    #     challenge_text= "Learn every day django atleast  20 min"

    # else:
    #     return  HttpResponseNotFound(" This month is not supported")

    # return HttpResponse(challenge_text)
