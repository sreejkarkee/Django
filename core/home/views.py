from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.



def home(request):
 return render(request, 'home/index.html')  



def success_page(request):
    print("Success page accessed")
    return HttpResponse("<h1>Success!</h1>")