from rest_framework.routers import SimpleRouter
from django.urls import path
# from django.urls import include, re_path
from .views import (
    TestView
)

urlpatterns = [
    path("test", TestView.as_view(), name="test"),
]
