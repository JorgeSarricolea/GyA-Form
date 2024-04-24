from django.urls import path
from .views import show_form, create_prospect

urlpatterns = [
    path('', show_form),
    path('new/', create_prospect),
]
