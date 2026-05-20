from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="recipe_list"),
    path('add/', views.add , name="add_recipe"),
    path('edit/<int:ID>/', views.edit ,name="edit_recipe"),
    path('delete/<int:ID>/', views.delete ,name="delete_recipe"),
]
