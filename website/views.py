from django.shortcuts import render, redirect
from .models import Project, Contact
from django.core.mail import send_mail

def home(request):
    projects = Project.objects.all().order_by('-created_at')

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save to database
        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )
        send_mail(
            subject="New Client Message from Website",
            message=f"Name: {name}\nEmail: {email}\nMessage: {message}",
            from_email=None,
           recipient_list=["kamsaa0001@gmail.com"],
        )

        return redirect("/?success=true")

    return render(request, "website/home.html", {"projects": projects})