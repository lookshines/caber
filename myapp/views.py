from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about-us.html")

def services(request):
    return render(request, "services.html")

def hse(request):
    return render(request, "hse.html")

def contact(request):
    return render(request, "contact.html")