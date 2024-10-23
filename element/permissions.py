from rest_framework import permissions


class IsActive(permissions.BasePermission):
    """
    Проверяет, активен ли пользователь.
    """

    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        return False
