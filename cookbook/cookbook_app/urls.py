from django.urls import path
from .views import New_recipe
from . import views

urlpatterns = [
    path('', views.base, name='cookbook-app-base'),
    path('home/', views.home, name='cookbook_app-home'),
    path('about/', views.about, name='cookbook_app-about'),
     path('new_recipe/', New_recipe.as_view(), name='cookbook_app-new_recipe'),
]
