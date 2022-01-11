from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('api/', include('api.urls', namespace='api')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),

]
