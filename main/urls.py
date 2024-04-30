from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('prospects.urls')),
    path('admin/', admin.site.urls),
    path('prospects/', include('prospects.urls')),
]
