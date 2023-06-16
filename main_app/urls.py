from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shrooms/', views.shrooms_index, name='index'),
    path('shrooms/<int:shroom_id>/', views.shrooms_show, name='show'),
    path('shrooms/create/', views.ShroomCreate.as_view(), name='shroom_create'),
    path('shrooms/<int:pk>/update/', views.ShroomUpdate.as_view(), name='shroom_update'),
    path('shrooms/<int:pk>/delete/', views.ShroomDelete.as_view(), name='shroom_delete'),
    path('shrooms/<int:shroom_id>/add_origin', views.add_origin, name='add_origin'),
    path('meals/', views.MealList.as_view(), name='meal_list'),
    path('meals/<int:pk>', views.MealDetail.as_view(), name='meal_detail'),
    path('meals/create', views.MealCreate.as_view(), name='meal_create'),
    path('meals/<int:pk>/update/', views.MealUpdate.as_view(), name='meal_update'),
    path('meals/<int:pk>/delete/', views.MealDelete.as_view(), name='meal_delete'),
]