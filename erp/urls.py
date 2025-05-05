from django.urls import path

from .views import *

urlpatterns = [
    # Category URLs
    path('categories/', CategoryApiView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryApiView.as_view(), name='category-detail'),

    # Course URLs
    path('courses/', CourseApiView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseApiView.as_view(), name='course-detail'),

    # Teacher URLs
    path('teachers/', TeacherApiView.as_view(), name='teacher-list'),
    path('teachers/<int:pk>/', TeacherApiView.as_view(), name='teacher-detail'),

    # Group URLs
    path('groups/', GroupApiView.as_view(), name='group-list'),
    path('groups/<int:pk>/', GroupApiView.as_view(), name='group-detail'),

    # Module URLs
    path('modules/', ModuleApiView.as_view(), name='module-list'),
    path('modules/<int:pk>/', ModuleApiView.as_view(), name='module-detail'),

    # Homework URLs
    path('homeworks/', HomeworkApiView.as_view(), name='homework-list'),
    path('homeworks/<int:pk>/', HomeworkApiView.as_view(), name='homework-detail'),
    path('homeworks/<int:pk>/download/', HomeworkDownloadApiView.as_view(), name='homework-download'),

    # Video URLs
    path('videos/', VideoApiView.as_view(), name='video-list'),
    path('videos/<int:pk>/',VideoApiView.as_view(), name='video-detail'),

    # Student URLs
    path('students/', StudentApiView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentApiView.as_view(), name='student-detail'),

    # Count URLs
    path('count/', CountApiView.as_view(), name='count-list'),
]
