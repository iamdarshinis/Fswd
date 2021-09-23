from django.shortcuts import render
from django.http import HttpResponse
from website.models import Contact_us 

# Create your views here.
def index(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,"aboutus.html")

def testimonials(request):
    return render(request,"testimonials.html")

def gallery(request):
    return render(request,"gallery.html")

def contactus(request):
    if request.method=="POST":
        nam = request.POST["name"]
        emai = request.POST["email"]
        numbe = request.POST["number"]
        messag = request.POST["message"]

        data = Contact_us(name=nam,email=emai,number=numbe,message=messag)
        data.save()
        return render(request,"gratitude.html")

    return render(request,"contactus.html")

def media(request):
    return render(request,"media.html")

def gratitude(request):
    return render(request,"gratitude.html")