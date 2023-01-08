from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('api/v1/', include("api.urls")),    
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
]
