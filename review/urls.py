from django.urls import path
from . import views

urlpatterns = [
    path('book/all', views.all, name='book_all'),
    path('book/<str:book_id>', views.read, name='book-detail')
]
