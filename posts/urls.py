from django.urls import path
from posts import views

urlpatterns = [
    path('', views.PostsFeedView.as_view(), name='feed'),
    path('create_post/', views.CreatePostView.as_view(), name='create_post')
]
