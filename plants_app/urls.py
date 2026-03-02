from django.urls import path 
from .import views 

urlpatterns = [
    path('', views.home, name='home'), 
    path('plants/', views.PlantList.as_view(), name='plant-list'), 
    path('plants/create/', views.PlantCreate.as_view(), name='plant-create'), 
    path('plants/<int:pk>/', views.PlantDetail.as_view(), name='plant-detail'), 
    path('plants/<int:pk>/edit/', views.PlantUpdate.as_view(), name='plant-update'),
    path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plant-delete'), 
]
