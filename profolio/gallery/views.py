from django.shortcuts import render

# Create your views here.
from gallery.models import Gallery

def home(request):
    gallerys = Gallery.objects.all()
    return render(request,'gallery/index.html',{'galleries':gallerys})