from django.urls import path
from .views import New_recipe
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from account.views import registration_view, logout_view, profile_view, login_view

urlpatterns = [
    path('', views.base, name='cookbook-app-base'),
    path('about/', views.about, name='cookbook_app-about'),
    path('new_recipe/', New_recipe.as_view(), name='cookbook_app-new_recipe'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
   # path('search/', search, name='cookbook_app-search'),
]
