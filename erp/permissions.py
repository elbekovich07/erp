from datetime import time
from datetime import timedelta

from django.utils import timezone
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrTeacherOrSelf(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user

        if user.is_staff:
            return True

        if user.groups.filter(name='teacher').exists():
            return True

        if user.groups.filter(name='student').exists():
            return request.method in SAFE_METHODS and obj.user == user

        return False


class IsPostEditable(BasePermission):
    message = 'You can only edit posts within 2 hours.'

    def has_object_permission(self, request, view, obj):
        if request.method in ['PATCH', 'PUT']:
            time_diff = timezone.now() - obj.created_at
            return time_diff <= timedelta(hours=2)
        return True


class IsWithInWorkingHours(BasePermission):
    pass
    # message = ('Oops!!!',
    #            'Sorry, working hours are from 9:00 to 18:00')
    #
    # def has_permission(self, request, view):
    #     now = timezone.localtime().time()
    #
    #     start_time = time(9, 0)
    #     end_time = time(20, 0)
    #
    #     return start_time <= now <= end_time

class WeekdayOnly(BasePermission):
    pass
    #
    # message = 'Sorry, today is not a working day.'
    #
    # def has_permission(self, request, view):
    #     now = timezone.localtime().time()
    #     return timezone.now().weekday() < 7
    #



