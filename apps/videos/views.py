import pytest
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi as yasg_openapi
from django.http import StreamingHttpResponse
from apps.users.models import User
from django.shortcuts import render, redirect, get_object_or_404
# from .forms import VideoForm
from django.urls import reverse
from django.http import JsonResponse
import cv2
import time
from .models import VideoSegment
from datetime import datetime, timedelta
from .tasks import consume_rtsp_stream

class TestView(APIView):
  def get(self, request):
    users = User.objects.all()
    return Response("Hello this fucking world!!!")

# def segment_list_view(request, video_id):
#     video = Video.objects.get(pk=video_id)
#     segments = Frame.objects.filter(video=video)
#     return render(request, 'videos/segment_list.html', {'video': video, 'segments': segments})


# def upload_video(request):
#     if request.method == 'POST':
#         form = VideoForm(request.POST, request.FILES)
#         if form.is_valid():
#             video = form.save()
#             return redirect(reverse('videos:show_video', args=[video.id])) 
#     else:
#         form = VideoForm()
#     return render(request, 'videos/upload_video.html', {'form': form})

# def show_video(request, video_id):
#     video = get_object_or_404(Video, pk=video_id)
#     return render(request, 'videos/show_video.html', {'video': video})

# def start_rtsp_stream(request):
# 	task = consume_rtp_stream_task.apply_async()
# 	return JsonResponse({'task_id': task.id})

def consume_rtsp_stream_task(request):
	#should get from the request, temporary hardcode for now
	rtsp_url = 'rtsp://admin:L2427AA6@192.168.1.3:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif'
	output_file_prefix = 'camera_001'
 
	if not (rtsp_url and output_file_prefix):
		return JsonResponse({'error': 'Missing RTSP stream URL or output file name'}, status=400)
 
	consume_rtsp_stream.delay(rtsp_url, output_file_prefix)
 
	return JsonResponse({'message': 'RTSP stream store successfully'})
