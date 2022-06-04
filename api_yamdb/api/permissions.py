from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif ( request.user.is_authenticated
            and request.user.is_admin):
            return True
        elif ( request.user.is_superuser):
            return True
