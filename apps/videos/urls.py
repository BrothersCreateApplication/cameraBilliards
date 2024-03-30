from rest_framework.routers import SimpleRouter
from django.urls import path
# from django.urls import include, re_path
from .views import (
    TestView, 
    segment_list_view, 
    segment_list_default_view,
    consume_rtsp_stream_task
    # upload_video, show_video
)

urlpatterns = [
    path("test", TestView.as_view(), name="test"),
    path('<str:camera_id>/segment/<str:segment_id>/', segment_list_view, name='segment_list'),
    path('<str:camera_id>/segment/', segment_list_default_view, name='segment_default_list'),
    path('start-stream', consume_rtsp_stream_task, name='start-stream'),
    # path('upload/', upload_video, name='upload_video'),
    # path('<str:video_id>/', show_video, name='show_video'),
]
