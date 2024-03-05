from rest_framework.routers import SimpleRouter
from django.urls import path
from django.conf.urls import url
from django.urls.conf import include
from .views import (
    LoginView,
    UserView,
    RegisterView,
    LoginGoogleView,
    LoginFacebookView,
    LoginAppleView,
    RequestOTPEmailView,
    VerifyOTPEmailView,
    HighLevelUserViewSet,
    ContestScoreView,
    AdRewards1TokenView
)

router = SimpleRouter(trailing_slash=False)
router.register(r'^leaderboard$', HighLevelUserViewSet, basename="leaderboard-level")

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register", RegisterView.as_view(), name="register"),
    path("sign-in", RequestOTPEmailView.as_view(), name="sign-in"),
    path("profile/me", UserView.as_view(), name="profile-me"),
    path(
        "login-google",
        LoginGoogleView.as_view(),
        name="login-google",
    ),
    path(
        "login-facebook",
        LoginFacebookView.as_view(),
        name="login-facebook",
    ),
    path(
        "login-apple",
        LoginAppleView.as_view(),
        name="login-apple",
    ),
    path("verify-otp", VerifyOTPEmailView.as_view(), name="verify-otp"),
    path("contest-score", ContestScoreView.as_view(), name="contest-score"),
    path("ad-rewards-1-hra", AdRewards1TokenView.as_view(), name="ad-rewards-1-hra"),
    url('', include(router.urls)),
]
