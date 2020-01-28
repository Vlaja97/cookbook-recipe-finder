from django.urls import path
from .views import New_recipe
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.base, name='cookbook-app-base'),
    path('about/', views.about, name='cookbook_app-about'),
    path('new_recipe/', New_recipe.as_view(), name='cookbook_app-new_recipe'),
]

urlpatterns += staticfiles_urlpatterns()