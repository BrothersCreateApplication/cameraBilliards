from model_bakery import baker
import pytest
from rest_framework.test import APIClient
from django.urls import reverse


@pytest.fixture
def user():
    return baker.make_recipe("apps.users.tests.user")


@pytest.fixture
def authenticated_client(user):
    client = APIClient()
    url = reverse("users:login")
    response = client.post(
        reverse("users:login"),
        data={
            "email": user.email, 
            "password": "test123123",
            "device_id": "1407",
            "app_version": "macos",
            "os_version": "11.0.1",
            "platform": "web"},
        format="json",
    )
    client.credentials(HTTP_AUTHORIZATION="JWT " + response.data["access_token"])
    return client

@pytest.fixture
def user_login():
    return baker.make_recipe("apps.users.tests.user_login")