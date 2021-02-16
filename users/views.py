from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet

from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
