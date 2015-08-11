from django.shortcuts import render, get_object_or_404
from .models import TopicArea, CatalogueItem



# Create your views here.
def home(request):
    topics = TopicArea.objects.filter(active=True).order_by('name')
    return render(request, "home.html", {'topics': topics})


def topic_content(request, pk):
    content = CatalogueItem.objects.filter(topic_area_id=pk)
    return render(request, "content_list.html", {'content': content})
