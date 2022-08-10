from urllib import request
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from .models import Book
import json
