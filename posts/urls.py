from django.urls import path
from posts import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('feed/', views.PostFeed.as_view()),
]
