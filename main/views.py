from django.shortcuts import render
from .models import GalleryImage


def index(request):
    return render(request, 'main/index.html')


def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'main/gallery.html', {'images': images})
