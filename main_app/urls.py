from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shrooms/', views.shrooms_index, name='index'),
    path('shrooms/<int:shroom_id>/', views.shrooms_show, name='show')
]