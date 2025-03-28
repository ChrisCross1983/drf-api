from django.urls import path
from .views import PostList, PostDetail, PostFeed, AllPosts

urlpatterns = [
    path('', PostList.as_view(), name='create-post'),
    path('<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('feed/', PostFeed.as_view(), name='post-feed'),
    path('all/', AllPosts.as_view(), name='all-posts'),
]
