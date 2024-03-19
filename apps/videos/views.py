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

class TestView(APIView):
  def get(self, request):
    users = User.objects.all()
    return Response("Hello world!!!")

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
