from urllib import request
from django.shortcuts import get_object_or_404, redirect, render
from .models import Book


def all(request):
    object_list = Book.objects.all()  # 이거를 json으로 못넘기나?
    return render(request, 'Blog/home.html', {'object_list': object_list})


def read(request, book_id):
    object_detail = get_object_or_404(Book, id=book_id)  # id가 뭐지?
    return render(request, 'Blog/page_detail.html', {'object_detail': object_detail})
# Create your views here.
