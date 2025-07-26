from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os

def serve_nextjs_index(request):
    index_path = os.path.join(settings.BASE_DIR, 'static', 'index.html')
    with open(index_path, 'r', encoding='utf-8') as file:
        return HttpResponse(file.read())