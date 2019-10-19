from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.detail, name='detail'),
    path('kind/<str:k>/', views.kind, name='kind'),
    path('about', views.about, name='about'),
]