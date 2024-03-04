import pytest
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi as yasg_openapi
from django.http import StreamingHttpResponse

class TestView(APIView):
  def get(self, request):
    return Response("Hello world!!!")
