
from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/profile/edit', views.profile_edit, name='profile_edit'),
    path('mypage/', views.mypage, name='mypage')
]
