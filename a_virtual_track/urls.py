from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('b_home.urls'), name="home"),
    path('summernote/', include('django_summernote.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('c_users.urls')),
]
