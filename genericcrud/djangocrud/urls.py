from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.ItemViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('items/<int:pk>/', views.ItemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
