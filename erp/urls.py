from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, CourseViewSet, ModuleViewSet, HomeworkViewSet, StudentApiView, TeacherViewSet, \
    VideoViewSet, GroupViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'homeworks', HomeworkViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/students/', StudentApiView.as_view()),
    path('api/students/<int:pk>/', StudentApiView.as_view()),

]
