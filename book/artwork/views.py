from django.shortcuts import render

from author.models import Author
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


def listing(request):
    author_list = Author.objects.filter(available=True)
    paginator = Paginator(author_list, 3)
    page = request.GET.get('page')
    try:
        authors = paginator.page(page)
    except PageNotAnInteger:
        authors = paginator.page(1)
    except EmptyPage:
        authors = paginator.page(paginator.num_pages)
    context = {
        'authors': authors,
        'paginate': True
    }
    return render(request, 'artwork/listing.html', context)