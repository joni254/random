from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse




# Flights views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request,"flights/login.html",{"message":None})
    context = {
        "user":request.user,
        "Flights":Flight.objects.all()
    }
    return render(request, "flights/index.html",context)

#Login view goes here.
def login_view(request):
    username= request.POST["username"]
    password= request.POST["password"]
    user= authenticate(request, username=username, password=password)
    if user is not None:
        login(request,user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request,"flights/login.html",{"message":"Wrong username or password!"})
#flight view goes here.
def flight(request, flight_id):
    if not request.user.is_authenticated:
        return render(request,"flights/login.html",{"message":None})
    try:
        flight =Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("FLIGHT DOES NOT EXIST.")
    context = {
        "flight":flight,
        "passangers":flight.passangers.all(),
        "non_passangers":Passanger.objects.exclude(flights=flight).all()
    }
    return render(request,"flights/flight.html",context)

# This is a vook view.
def book(request, flight_id):
    try:
        passanger_id= int(request.POST["passanger"])
        passanger = Passanger.objects.get(pk=passanger_id)
        flight = Flight.objects.get(pk=flight_id)

    except KeyError:
          return render(request,"flights/error.html",{"message":"No Selection Made."})

    except Flight.DoesNotExist:
         return render(request,"flights/error.html",{"message":"No Flight Found."})
    except Passanger.DoesNotExist:
         return render(request,"flights/error.html",{"message":"No Passanger Found."})

    passanger.flights.add(flight)
    return HttpResponseRedirect(reverse("flight", args=(flight_id,)))

# This is the logout view.
def logout_view(request):
    logout(request)
    return render(request,"flights/login.html",{"message":"You are logged out successfully."})
