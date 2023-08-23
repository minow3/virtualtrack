from django.urls import path
from .views import UserRegisterView, UserEditView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', UserEditView.as_view(), name='profile'),
]