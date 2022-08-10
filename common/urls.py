
from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/profile/edit', views.profile_edit, name='profile_edit'),
    path('mypage/', views.mypage, name='mypage'),
    path('book/<str:book_id>', views.read, name='book-detail'),
]
