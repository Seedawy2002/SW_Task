from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from kpi.views import home_view  # Import your home view

urlpatterns = [
    path('', home_view, name='home'),  # Route for the home page
    path('admin/', admin.site.urls),
    path('api/', include('kpi.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='api-schema'), name='redoc'),
]
