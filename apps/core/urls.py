from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('projects/', views.projects, name='projects'),
]
