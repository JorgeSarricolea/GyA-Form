from django.urls import path
from .views import show_form

urlpatterns = [
    path('', show_form),
]
