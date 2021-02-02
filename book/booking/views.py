from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django import forms
from artwork.models import Artwork
from booking.models import Contact, Booking
from .forms import ContactForm, ParagraphErrorList
from django.db import transaction

# Create your views here.
@transaction.atomic
def detail(request, artwork_id):
    artwork = get_object_or_404(Artwork, pk= album_id)
    author_name = " ".join([author.name for author in artwork.authors.all()])

    context = {
        'artwork.title': artwork.title,
        'author_name': author_name,
        'artwork.id': artwork.id,
        'thumbnail': artwork.photo,
    }

    if request.method == 'POST':
        form = ContactForm(request.POST, error_class=ParagraphErrorList)
        if form.is_valid():

            email = form.cleaned_data['email']
            name = form.cleaned_data['name']

            contact = Contact.objects.filter(email=email)
            if not contact.exists():
                # If a contact is not registered, create a new one.
                contact = Contact.objects.create(
                    email=email,
                    name=name
                )
            else:
                contact = contact.first()
            # If no album matches the id, it means the form must have been tweaked
            # so returning a 404 is the best solution.
            artwork = get_object_or_404(Artwork, id=artwork_id)
            booking = Booking.objects.create(
                contact=contact,
                album=artwork
            )
            # Make sure no one can book the album again.
            artwork.available = True
            artwork.save()
            context = {
                'artwork_title': artwork.title
            }
            return render(request, 'booking/merci.html', context)
        else:
            context['errors'] = form.errors.items()
    else:
        form = ContactForm()

    context['form'] = form
    return render(request, 'booking/detail.html', context)




def search(request):
    query = request.GET.get('query')
    if not query:
        artworks = Artwork.objects.all()
    else:
        artworks = Artwork.objects.filter(title__icontains=query)

        if not Artworks.exists():
            artworks = Artwork.objects.filter(authors__name__icontains=query)

    title = "Résultats pour la requete %s"%query
    context = {
        'artworks': artworks,
        'title': title,
    }
    return render(request, 'booking/search.html', context)


class NouvArt(forms.Form):
    title = forms.CharField()
    photo = forms.FileField()
    reference = forms.IntegerField()
    created_at = forms.DateTimeField()
    available = forms.BooleanField()

def nouv_art(request):
    sauvegarde = False
    form = NouvAlb(request.POST or None, request.FILES)
    if form.is_valid():
        artwork = Artwork()
        artwork.title = form.cleaned_data["title"]
        artwork.photo = form.cleaned_data["photo"]
        artwork.reference = form.cleaned_data["reference"]
        artwork.created_at = form.cleaned_data["created_at"]
        artwork.available = form.cleaned_data["available"]
        artwork.save()
        sauvegarde = True

    return render(request, 'art_form.html', {
        'form': form,
        'sauvegarde': sauvegarde
    })


def voir_artworks(request):
    return render(
        request,
        'voir_artwork.html',
        {'artworks': Artwork.objects.all()}
    )
