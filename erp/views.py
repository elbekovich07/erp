from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from erp.models import *
from erp.serializers import CategorySerializer, CourseModelSerializer, TeacherSerializer, GroupSerializer, \
    ModuleSerializer, \
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
        serializer = CourseModelSerializer(courses, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def count(self, request):
        return Response({'total_categories': Category.objects.count()})


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer
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


class StudentApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return Response({"message": "Student deleted successfully."}, status=status.HTTP_204_NO_CONTENT)




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


