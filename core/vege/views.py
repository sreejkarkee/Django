from django.shortcuts import render, redirect
from .models import Receipe


def receipes(request):
    if request.method == "POST":
        receipe_name = request.POST.get("receipe_name")
        receipe_description = request.POST.get("receipe_description")
        receipe_image = request.FILES.get("receipe_image")

        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image,
        )

        return redirect("/receipes/")

    queryset = Receipe.objects.all()
    context = {"receipes": queryset}

    return render(request, "receipes.html", context)