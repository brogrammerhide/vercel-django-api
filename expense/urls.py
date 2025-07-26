from django.urls import path
from expense.views import index

urlpatterns = [
    path('', index),
]
