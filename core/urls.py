"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (
     TokenObtainPairView,
     TokenRefreshView)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import  openapi

#creating schema view
schema_view = get_schema_view(
    openapi.Info(
        title="E-commerce API",
        default_version="v1",
        description="This is an E-commerce API for shopping electronic gadgets",
        contact=openapi.Contact(email="iampatrickugo@gmail.com"),
        license=openapi.License(name='MIT License'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('userapp.urls')),
    path("", include('products.urls')),
    path("", include('productorder.urls')),


    # Authentication urls
    path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #docs
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui"),
    path('docs/', schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),

]


urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)