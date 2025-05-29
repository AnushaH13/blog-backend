from django.urls import path
from .views import BlogListCreate

urlpatterns = [
    path('blogs/', BlogListCreate.as_view(), name='blog-list-create'),
]
