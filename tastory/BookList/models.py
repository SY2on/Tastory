from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.TextField()   
    img_url = models.TextField()      
    author = models.TextField(max_length=20)    
    book_info = models.TextField()
    isbn = models.TextField(max_length=20)
    pubdate = models.DateField()
    publisher = models.TextField(max_length=20)
    dt_created = models.DateField(auto_now=True)
    
    def __str__(self):                                   
        return self.title