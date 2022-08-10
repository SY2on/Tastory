from urllib import request
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from .models import Book
import json


def all(request):
    object_list = Book.objects.all()
    return render(request, 'X.html', {'object_list': object_list})


def read(request, book_id):
    with open('./review/testA.json', 'r', encoding='UTF8') as f:
        json_data = json.load(f)

    for data in json_data:
        if data["isbn"] == str(book_id):
            sendData = data
            break
    print(sendData)
    return render(request, {'object_detail': sendData})
    # return JsonResponse(sendData)
    # return HttpResponse(json.dumps(data), content_type = "application/json")
    # Pull Request
