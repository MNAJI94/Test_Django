from django.shortcuts import render

# Create your views here.

def index(request):
    albums = Album.objects.filter(available = True).order_by('-created_at')[:12]
    context = {'albums': albums}
    return render(request, 'author/index.html', context)