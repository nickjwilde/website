from django.shortcuts import render

from .models import Skill

# Create your views here.
def home(request):
    return render(request, 'nickjwilde/home.html', None)

def about(request):
    skills = Skill.objects.all().order_by('-num_years')
    context = {'skills': skills}
    return render(request, 'nickjwilde/about.html', context)
