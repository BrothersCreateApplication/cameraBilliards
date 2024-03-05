from model_bakery import baker
from model_bakery.recipe import Recipe, foreign_key
from apps.flax_id import get_flax_id
from apps.users.models import User, UserLogin
from django.contrib.auth.hashers import make_password


baker.generators.add("apps.flax_id.django.fields.FlaxId", get_flax_id)

password = make_password("test123123")
user = Recipe(User, email="test@mail.com", password=password, valid_access_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg2OTcyOTYwLCJqdGkiOiJjYTU5YjcxMjY4NWI0MzJhODJlN2Y5MjUxN2RhMDFhYSIsInVzZXJfaWQiOiJEVmhGMnhNUEZqeWNiX251In0.b1fSLwrCgj7IHuicuICEnFNitHpEAicZXuGrItQrDu4", is_active=True)

user_login = Recipe(UserLogin, device_id = "1234", app_version="beta:1.0.0", os_version="macos:11.0.0", platform="ios")