from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Skill, Project, Experience, Certification
from .forms import ContactForm

def home(request):
    # Fetch data
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.order_by('-start_date') # Fix typo in original thought
    certifications = Certification.objects.all()
    
    for exp in experiences:
        if exp.description:
            exp.description_list = [item.strip() for item in exp.description.split(".")]
        else:
            exp.description_list = []
    
    # Form Handling
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully!')
            return redirect('home')
    else:
        form = ContactForm()

    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects,
        'experiences': experiences,
        'certifications': certifications,
        'contact_form': form
    }
    return render(request, 'portfolio/home.html', context)


def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, "portfolio/projects.html", context)