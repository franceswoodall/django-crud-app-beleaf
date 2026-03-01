from django.urls import path 
from .import views 

urlpatterns = [
    path('', views.home, name='home'), 
    path('plants/', views.PlantList.as_view(), name='plant-list'), 
    path('plants/create/', views.PlantCreate.as_view(), name='plant-create'), 
]
