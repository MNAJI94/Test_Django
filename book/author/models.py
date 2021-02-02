from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField('Author name', max_length=200, unique = False)

    # def __str__(self):
    #     return self.name

    class Meta:
        verbose_name = "author"