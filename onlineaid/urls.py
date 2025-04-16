from django.contrib import admin
from django.urls import path, include


# from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from members.views import RegisterUserView

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/register/', RegisterUserView.as_view(), name='register'),  # ✅ NEW
    # path('api-auth/', include('rest_framework.urls'))
    path('', include('members.urls')),
    path('admin/', admin.site.urls),
]
