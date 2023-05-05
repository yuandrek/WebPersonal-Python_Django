

from django.shortcuts import render
from .models import proyecto
from .models import slider

# Create your views here.
def portfolio(request):
    projects = proyecto.objects.all()
    sliderdata = slider.objects.all()
    return render(request, 'index.html', {'projects':projects, 'sliderdata':sliderdata})