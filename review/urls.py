from django.urls import path
from . import views

urlpatterns = [
    path('book/all', views.all, name='book_all'),
    path('book/<int:book_id>', views.read, name='book-detail')
]
