from django.urls import path
from . import views

urlpatterns = [
    path('review/write/', views.write, name='review_write'),
    path('review/<int:review_id>/', views.detail, name='review_detail'),
    path('review/<int:review_id>/edit/', views.edit, name='review_edit'),
    path('', views.main, name='main'),
    path('search/', views.search, name='book_search'),
    #path('book/<int:book_id>', views.bookinfo, name='book_detail'),
]
