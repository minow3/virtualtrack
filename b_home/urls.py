from django.urls import path
from . import views
from .views import PostDetailView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
]
