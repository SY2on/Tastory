from django.urls import path
from . import views

urlpatterns = [
    path('review/write/', views.write, name='review_write'),
    path('review/<int:review_id>/', views.detail, name='review_detail'),
    path('review/<int:review_id>/edit/', views.edit, name='review_edit'),
    # path('book/all', views.all, name='book_all'),
    # path('book/<str:book_id>', views.read, name='book-detail'),
    ]
