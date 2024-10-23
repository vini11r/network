from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserSerializer, UserCreateUpdateSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()

    def get_serializer_class(self):
        if self.action in ["create", "update"]:
            return UserCreateUpdateSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (AllowAny,)
        elif self.action == "list":
            self.permission_classes = (IsAuthenticated,)
        elif self.action in ["retrieve", "update", "destroy", "partial_update"]:
            self.permission_classes = (IsAuthenticated,)
        return super().get_permissions()
