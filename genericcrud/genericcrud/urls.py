from django.contrib import admin
from django.urls import path, include  # Adicione 'include' aqui

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('djangocrud.urls')),  # Adicione esta linha
]