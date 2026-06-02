from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def index(request):

    if request.method == "POST":

        Contact.objects.create(
            name=request.POST.get("name"),
            surname=request.POST.get("surname"),
            email=request.POST.get("email"),
            message=request.POST.get("message")
        )

        messages.success(request, "Message sent successfully!")

        return redirect("index")

    return render(request, "form/index.html")
