from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from erp.models import *
from erp.serializers import CategorySerializer, CourseSerializer, TeacherSerializer, GroupSerializer, ModuleSerializer, \
    HomeworkSerializer, VideoSerializer, StudentSerializer


# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['name', ]
    ordering_fields = ['name', ]

    @action(detail=True, methods=['get'])
    def courses(self, request, pk=None):
        category = self.get_object()
        courses = category.courses.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def count(self, request):
        return Response({'total_categories': Category.objects.count()})


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['name', ]
    ordering_fields = ['name', ]

    def get_queryset(self):
        queryset = Course.objects.all()
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category__id=category_id)
        return queryset

    @action(detail=False, methods=['get'])
    def count(self, request):
        return Response({'total_courses': Course.objects.count()})


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['first_name', 'last_name', 'username']
    ordering_fields = ['first_name', 'last_name', ]

    @action(detail=False, methods=['get'])
    def count(self, request):
        return Response({'total_teachers': Teacher.objects.all().count()})


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['name', 'course__name']
    ordering_fields = ['name', 'started_at']

    @action(detail=False, methods=['get'])
    def count(self, request):
        return Response({'total_groups': Group.objects.all().count()})


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['name', 'module__name']
    ordering_fields = ['title', ]

    @action(detail=False, methods=['get'])
    def count(self, request):
        return Response({'total_modules': Module.objects.all().count()})


class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['overview', 'module__name']
    ordering_fields = ['deadline', ]

    @action(detail=False, methods=['get'])
    def count(self, request):
        return Response({'total_homeworks': Homework.objects.count()})


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']

    @action(detail=False, methods=['get'])
    def count(self, request):
        return Response({'total_videos': Video.objects.count()})


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['first_name', 'last_name', 'phone_number', 'student_code']
    ordering_fields = ['first_name', 'last_name']

    @action(detail=False, methods=['get'])
    def count(self, request):
        return Response({'total_students': Student.objects.count()})
