from django.http import HttpResponse
from django.shortcuts import render
from .models import Place,Team
# Create your views here.
def demo(request):
    places=Place.objects.all()
    mteam=Team.objects.all()
    return render(request,"index.html",{'result':places,'teams':mteam})
def home(request):
    return render(request,"home.html")