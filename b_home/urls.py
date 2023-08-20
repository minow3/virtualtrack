from django.urls import path
from . import views
from .views import PostDetailView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('post/update/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('post/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
]
