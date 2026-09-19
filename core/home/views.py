from django.http import HttpResponse, request
from django.shortcuts import render


# Create your views here.



def home(request):
    people=[
        {'name':'Alice', 'age': 10},
        {'name':'Bob', 'age': 25},
        {'name':'Charlie', 'age': 13},
        {'name':'David', 'age': 40},
        {'name':'Eve', 'age': 32}
    ]
    
    return(render(request, 'home/index.html', context={'people':people}))



def success_page(request):
    print("Success page accessed")
    return HttpResponse("<h1>Success!</h1>")


def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')