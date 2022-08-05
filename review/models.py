from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.TextField()
    img_url = models.TextField()
    author = models.TextField()
    book_info = models.TextField()
    isbn = models.TextField(unique=True)
    pubdate = models.DateField()
    publisher = models.TextField()
    category = models.TextField()

    def __str__(self):
        return self.title
