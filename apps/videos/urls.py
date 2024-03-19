from rest_framework.routers import SimpleRouter
from django.urls import path
# from django.urls import include, re_path
from .views import (
    TestView, 
    # segment_list_view, upload_video, show_video
)

urlpatterns = [
    path("test", TestView.as_view(), name="test"),
    # path('<str:video_id>/segment/', segment_list_view, name='segment_list'),
    # path('upload/', upload_video, name='upload_video'),
    # path('<str:video_id>/', show_video, name='show_video'),
]
