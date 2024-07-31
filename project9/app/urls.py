from django.urls import path
from .views import *

urlpatterns = [
    path('register', register, name='register'),
    path('insert_topic', insert_topic, name='insert_topic'),
    path('insert_author', insert_author, name='insert_author'),
    path('insert_book', insert_book, name='insert_book')
]
