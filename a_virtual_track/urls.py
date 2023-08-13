from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('b_home.urls')),
    path('summernote/', include('django_summernote.urls')),
]
