from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow User Only to Update Their Own Profile"""

    def has_object_permission(self, request, view, obj):
        """Check User is Updating his own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
