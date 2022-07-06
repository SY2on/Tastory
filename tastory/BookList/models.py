from django.db import models

# Create your models here.

class BestBookList(models.Model):
    title = models.TextField()         
    author = models.TextField()    
    content = models.TextField()
    dt_created = models.DateField(auto_now=True)
    
    def __str__(self):                                   
        return self.title