from django.shortcuts import render
from .models import Author
# Create your views here.

def index(request):
    author = Author.objects.filter(available = True).order_by('-created_at')[:12]

    def splt(author):
        dico = {'value1':[], 'value2':[]}
        tab = author.split('-')
        for i in tab[0]:
            dico['value1'].append(i)
        for j in tab[1]:
            dico['value2'].append(j)
        return dico   
    
    return render(request, 'author/index.html', dico)

   

