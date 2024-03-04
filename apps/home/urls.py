from django.urls import path
from . import views
urlpatterns = [
    path('privacy-policy', views.policy),
    path('terms-of-use', views.termsofuse),
    path('support', views.support),
]
