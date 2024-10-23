from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (AllowAny,)
        elif self.action == "list":
            self.permission_classes = (IsAuthenticated,)
        elif self.action in ["retrieve", "update", "destroy", "partial_update"]:
            self.permission_classes = (IsAuthenticated,)
        return super().get_permissions()
