from django.urls import path
from .views import add_two_nums

urlpatterns = [
    path('', add_two_nums),
]