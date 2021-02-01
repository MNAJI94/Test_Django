from django.db import models
from artwork.models import Artwork
from contact.models import Contact

class Booking(models.Model):
    created_at = models.DateTimeField("date d'envoie",auto_now_add=True)
    contacted = models.BooleanField("demande traitée ?", default = False)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.contact)

    class Meta:
        verbose_name = "réservation"
