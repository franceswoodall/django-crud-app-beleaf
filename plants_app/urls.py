from django.urls import path 
from .import views 

urlpatterns = [
    path('', views.home, name='home'), 
    path('plants/', views.PlantList.as_view(), name='plant-list'), 
    path('plants/create/', views.PlantCreate.as_view(), name='plant-create'), 
    path('plants/<int:pk>/', views.PlantDetail.as_view(), name='plant-detail'), 
    path('plants/<int:pk>/edit/', views.PlantUpdate.as_view(), name='plant-update'),
    path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plant-delete'), 
    path('plants/<int:pk>/add-care/',
         views.add_care,
         name='add-care'), 
    path('categories/', views.CategoryList.as_view(), name='category-list'), 
    path('categories/create/', views.CategoryCreate.as_view(), name='category-create'), 
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail')
]
