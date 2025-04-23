from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, CourseViewSet, ModuleViewSet, HomeworkViewSet, StudentViewSet, TeacherViewSet, \
    VideoViewSet, GroupViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'homeworks', HomeworkViewSet)
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
