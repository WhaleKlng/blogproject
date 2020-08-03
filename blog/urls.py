from django.urls import path
from .views import PostViewSet

index = PostViewSet.as_view({'get': 'list'})

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index1'),
    path('posts/<int:pk>/', views.detail, name='detail'),
    path('kind/<str:k>/', views.kind, name='kind'),
    path('about', views.about, name='about'),
    # path('api/index/', views.IndexPostListView.as_view())
    path('api/index/', index)
]
