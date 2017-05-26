from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Skill
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, 'nickjwilde/home.html', None)

def about(request):
    skills = Skill.objects.all().order_by('-num_years')
    context = {'skills': skills}
    return render(request, 'nickjwilde/about.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, label_suffix='')

        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm(label_suffix='')
    return render(request, 'nickjwilde/contact.html', {'form': form})
