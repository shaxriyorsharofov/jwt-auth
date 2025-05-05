from django.urls import path
from .views import RegisterView, Test, LoginView, Logout, Test2
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('regis/', RegisterView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('test/', Test.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', Logout.as_view()),
    path('test2/', Test2.as_view())
]
