from django.urls import path
from .views import RegisterUserView, members, CustomLoginView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('api/register/', RegisterUserView.as_view(), name='register'),
    path('members/', members, name='members'),
    path('api/login/', CustomLoginView.as_view(), name='custom_login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
