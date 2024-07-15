from django.db import models
from django.db.models import enums
    
class Books(models.Model):

    class BookGenres(models.TextChoices):
        FICTION = 'Fiction'
        MYSTERY = 'Mystery'
        HORROR = 'Horror'
        ROMANCE = 'Romance'
        COMICS = 'Comics'
        CRIME = 'Crime'
        NOVEL = 'Novel'

    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=300)
    isbn = models.CharField(max_length=13)
    publication_year = models.IntegerField()
    publisher = models.CharField(max_length=300)
    genre = models.TextField(choices=BookGenres)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
