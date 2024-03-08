"""camera-billiards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,re_path
from django.urls.conf import include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from django.conf import settings
from django_otp.admin import OTPAdminSite
from django.conf import settings
from django.conf.urls.static import static
  
schema_view = get_schema_view(
    openapi.Info(
        title="Typemaster Backend API documentation",
        default_version="v1",
        description="Description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="nguyenvunhatduy@gmail.com"),
        license=openapi.License(name="Duy"),
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)
urlpatterns = [
    path('adad/', admin.site.urls),
    path("", include("apps.home.urls")),
    path("api/v1/videos/", include(("apps.videos.urls", "videos"), namespace="videos")),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
        ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

if settings.OTP_TOKEN_ENABLE:
    admin.site.__class__ = OTPAdminSite
