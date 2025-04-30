from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrTeacherOrSelf(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user

        if user.is_staff:
            return True

        if user.groups.filter(name='teacher').exists():
            return True

        if user.get_profile(name='student').exists():
            return request.method in SAFE_METHODS and obj.user == user

        return False