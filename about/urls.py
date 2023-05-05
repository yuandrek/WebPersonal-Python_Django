
from django.urls import path

from . import views

# Conf url
urlpatterns = [
    path('about/', views.about, name='about'),
]