from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def view1(request):
    print(request.method)
    return HttpResponse("Hello world i am from view1")

def view2(request):
    return HttpResponse("Hello world i am from view2")

def view3(request):
    return HttpResponse("Hello wor;d i am from view3")

def view4(request):
    return JsonResponse({"name":"harish","message" : "hello world"})

def view5(request):
    return JsonResponse({"status":"success","response":"Welcome"})

def dynamicview(request):
    qp1 = request.GET.get("name","world")
    return HttpResponse(f"hello {qp1}")

# Json always allow subject only

def personInfo(request):
    name = request.GET.get("name","harish")
    city = request.GET.get("city","hyd")
    role = request.GET.get("role","Trainer")
    info = {"name":name,"city":city,"role":role}
    return JsonResponse({"status":"success","data":info})

def moviereview(request):
    movie = request.GET.get("movie","Hellboy")
    showtime = request.GET.get("showtime","6pm")
    ticket_cost = request.GET.get("ticket_cost",250)
    total_no_of_tickets = request.GET.get("total_no_of_tickets",14)
    calc = int(ticket_cost) * int(total_no_of_tickets)
    total_price = request.GET.get("total_price",calc)
    info = {"movie":movie,"showtime":showtime,"ticket_cost":ticket_cost,"total_no_of_tickets":total_no_of_tickets,"total_price":total_price}
    return JsonResponse({"status":"success","data":info})

def temp1(request):
    return render(request,"./simple.html")
def temp2(request):
    return render(request,"./second.html")