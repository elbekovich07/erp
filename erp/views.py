
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from rest_framework import filters, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from erp.serializers import *
from .permissions import IsWithInWorkingHours, WeekdayOnly


class CategoryApiView(GenericAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated, IsWithInWorkingHours, WeekdayOnly]
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    lookup_field = 'pk'
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['name']
    ordering_fields = ['name']

    def get(self, request, pk=None):
        if pk:
            category = get_object_or_404(Category, pk=pk)
            serializer = self.get_serializer(category)
            return Response(serializer.data)
        categories = self.get_queryset()
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = self.get_serializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response({'message': 'Category deleted'}, status=status.HTTP_204_NO_CONTENT)


class CategoryCountApiView(APIView):
    permission_classes = [IsAuthenticated, IsWithInWorkingHours, WeekdayOnly]

    def get(self, request):
        return Response({'total_categories': Category.objects.count()})


class CourseApiView(GenericAPIView):
    serializer_class = CourseModelSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsWithInWorkingHours, WeekdayOnly]
    lookup_field = 'pk'
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['name']
    ordering_fields = ['name']


    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

    def get(self, request, pk=None):
        if pk:
            course = get_object_or_404(Course, pk=pk)
            serializer = self.get_serializer(course)
            return Response(serializer.data)
        courses = self.get_queryset()
        serializer = self.get_serializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        serializer = self.get_serializer(course, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        course.delete()
        return Response({'message': 'Course deleted'}, status=status.HTTP_204_NO_CONTENT)


class CourseCountApiView(APIView):
    permission_classes = [IsAuthenticated, IsWithInWorkingHours, WeekdayOnly]

    def get(self, request):
        return Response({'total_courses': Course.objects.count()})


class TeacherApiView(GenericAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    permission_classes = [IsAuthenticated, IsWithInWorkingHours, WeekdayOnly]
    lookup_field = 'pk'
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)

    def get(self, request, pk=None):
        if pk:
            teacher = get_object_or_404(Teacher, pk=pk)
            serializer = self.get_serializer(teacher)
            return Response(serializer.data)
        teachers = self.get_queryset()
        serializer = self.get_serializer(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        serializer = self.get_serializer(teacher, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        teacher.delete()
        return Response({'message': 'Teacher deleted'}, status=status.HTTP_204_NO_CONTENT)


class TeacherCountApiView(APIView):
    permission_classes = [IsAuthenticated, IsWithInWorkingHours, WeekdayOnly]

    def get(self, request):
        return Response({'total_teachers': Teacher.objects.count()})


class GroupApiView(GenericAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = [IsAuthenticated, IsWithInWorkingHours, WeekdayOnly]

    def get(self, request, pk=None):
        if pk:
            group = get_object_or_404(Group, pk=pk)
            serializer = self.get_serializer(group)
            return Response(serializer.data)
        groups = self.get_queryset()
        serializer = self.get_serializer(groups, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        group = get_object_or_404(Group, pk=pk)
        serializer = self.get_serializer(group, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        group = get_object_or_404(Group, pk=pk)
        group.delete()
        return Response({'message': 'Group deleted'}, status=status.HTTP_204_NO_CONTENT)


class GroupCountApiView(APIView):
    permission_classes = [IsAuthenticated, IsWithInWorkingHours, WeekdayOnly]

    def get(self, request):
        return Response({'total_groups': Group.objects.count()})


class ModuleApiView(GenericAPIView):
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [IsAuthenticated, IsWithInWorkingHours, WeekdayOnly]
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = super().get_queryset()
        course_id = self.request.query_params.get('course_id')
        if course_id:
            queryset = queryset.filter(course__id=course_id)
        return queryset

    def get(self, request, pk=None):
        if pk:
            module = get_object_or_404(Module, pk=pk)
            serializer = self.get_serializer(module)
            return Response(serializer.data)
        modules = self.get_queryset()
        serializer = self.get_serializer(modules, many=True)
        return Response(serializer.data)


class ModuleCountApiView(APIView):
    permission_classes = [IsAuthenticated, IsWithInWorkingHours, WeekdayOnly]

    def get(self, request):
        return Response({'total_modules': Module.objects.count()})


class HomeworkApiView(GenericAPIView):
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = super().get_queryset()
        module_id = self.request.query_params.get('module_id')
        if module_id:
            queryset = queryset.filter(module_id=module_id)
        return queryset

    def get(self, request, pk=None):
        if pk:
            homework = get_object_or_404(Homework, pk=pk)
            serializer = self.get_serializer(homework)
            return Response(serializer.data)
        homeworks = self.get_queryset()
        serializer = self.get_serializer(homeworks, many=True)
        return Response(serializer.data)


class HomeworkDownloadApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        homework = get_object_or_404(Homework, pk=pk)
        file_handle = homework.file.open()
        response = FileResponse(file_handle, as_attachment=True, filename=homework.file.name.split('/')[-1])
        return response


class HomeworkCountApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'total_homeworks': Homework.objects.count()})


class VideoApiView(GenericAPIView):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get(self, request, pk=None):
        if pk:
            video = get_object_or_404(Video, pk=pk)
            serializer = self.get_serializer(video)
            return Response(serializer.data)
        videos = self.get_queryset()
        serializer = self.get_serializer(videos, many=True)
        return Response(serializer.data)



class VideoCountApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'total_videos': Video.objects.count()})


class StudentApiView(GenericAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = [IsAuthenticated, IsWithInWorkingHours, WeekdayOnly]
    lookup_field = 'pk'

    def get(self, request, pk=None):
        if pk:
            student = get_object_or_404(Student, pk=pk)
            serializer = self.get_serializer(student)
            return Response(serializer.data)
        students = self.get_queryset()
        serializer = self.get_serializer(students, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        serializer = self.get_serializer(student, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return Response({'message': 'Student deleted'}, status=status.HTTP_204_NO_CONTENT)
