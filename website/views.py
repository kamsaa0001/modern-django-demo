from django.shortcuts import render
from .models import Project, Contact

def home(request):
    projects = Project.objects.all().order_by('-created_at')
    success = False

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save message in database
        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        success = True  # Show success message on same page

    return render(request, 'website/home.html', {
        'projects': projects,
        'success': success
    })