from django.urls import path
from .views import *

urlpatterns = [
    # Category URLs
    path('categories/', CategoryApiView.as_view(), name='category-list'),
    path('categories/count/', CategoryCountApiView.as_view(), name='category-count'),
    path('categories/<int:pk>/', CategoryApiView.as_view(), name='category-detail'),

    # Course URLs
    path('courses/', CourseApiView.as_view(), name='course-list'),
    path('courses/count/', CourseCountApiView.as_view(), name='course-count'),
    path('courses/<int:pk>/', CourseApiView.as_view(), name='course-detail'),

    # Teacher URLs
    path('teachers/', TeacherApiView.as_view(), name='teacher-list'),
    path('teachers/count/', TeacherCountApiView.as_view(), name='teacher-count'),
    path('teachers/<int:pk>/', TeacherApiView.as_view(), name='teacher-detail'),

    # Group URLs
    path('groups/', GroupApiView.as_view(), name='group-list'),
    path('groups/count/', GroupCountApiView.as_view(), name='group-count'),
    path('groups/<int:pk>/', GroupApiView.as_view(), name='group-detail'),

    # Module URLs
    path('modules/', ModuleApiView.as_view(), name='module-list'),
    path('modules/<int:pk>/', ModuleApiView.as_view(), name='module-detail'),
    path('modules/count/', ModuleCountApiView.as_view(), name='module-count'),

    # Homework URLs
    path('homeworks/', HomeworkApiView.as_view(), name='homework-list'),
    path('homeworks/<int:pk>/', HomeworkApiView.as_view(), name='homework-detail'),
    path('homeworks/<int:pk>/download/', HomeworkDownloadApiView.as_view(), name='homework-download'),
    path('homeworks/count/', HomeworkCountApiView.as_view(), name='homework-count'),

    # Video URLs
    path('videos/', VideoApiView.as_view(), name='video-list'),
    path('videos/<int:pk>/',VideoApiView.as_view(), name='video-detail'),
    path('videos/count/', VideoCountApiView.as_view(), name='video-count'),

    # Student URLs
    path('students/', StudentApiView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentApiView.as_view(), name='student-detail'),
]
