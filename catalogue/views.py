from django.shortcuts import render
from .models import TopicArea


# Create your views here.
def home(request):
    topics = TopicArea.objects.filter(active=True).order_by('name')
    return render(request, "home.html", {'topics': topics})
