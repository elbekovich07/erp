from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from erp.custom_oauth_token import CustomAuthToken, LogoutAPIView
from root import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('erp.urls')),
    path('api-auth/', include('rest_framework.urls')),

                  # API Docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(), name='redoc'),

                  # Token Auth
                  path('api/token-auth/', CustomAuthToken.as_view(), name='token-auth'),

                  # JWT Auth
                  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('api/login/', CustomAuthToken.as_view(), name='token_login'),
                  path('api/logout/', LogoutAPIView.as_view(), name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += debug_toolbar_urls()
