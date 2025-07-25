from django.urls import path
from src.api.expense.views import index

urlpatterns = [
    path('', index),
]
