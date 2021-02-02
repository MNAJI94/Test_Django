from django.db import models
from author.models import Author

# Create your models here.

class Artwork(models.Model):
    reference = models.IntegerField("référence", null=True)
    created_at = models.DateTimeField("date de création", auto_now_add=True)
    available = models.BooleanField("disponible", default=True)
    title = models.CharField('titre du disque ', max_length=200)
    photo = models.FileField("URL dl image", upload_to="photo/")
    authors = models.ManyToManyField(Author, related_name='arrtwork', blank=True)

    # def __str__(self):
    #     return self.title

    class Meta:
        verbose_name = "artwork"