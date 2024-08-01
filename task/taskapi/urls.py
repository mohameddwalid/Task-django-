from django.urls import path, include
from . import views

urlpatterns = [
    path('CreateProduct/', views.CreateProduct),
    path('FetchProduct/', views.FetchProduct),
    path("DeleteProduct/", views.DeleteProduct),
    path('UpdateProduct/',views.UpdateProduct),
    path('CreateInventory/', views.CreateInventory),
    path('FetchInventory/', views.FetchInventory),
    path("DeleteInventory/", views.DeleteInventory),
    path('UpdateInventory/',views.UpdateInventory),
    path("Joinning/",views.Joinning),   
]