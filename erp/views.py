from django.core.cache import cache
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import filters
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from erp.serializers import *
from .permissions import IsWithInWorkingHours, WeekdayOnly


@method_decorator(cache_page(60), name='get')
class CategoryApiView(GenericAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated, IsWithInWorkingHours, WeekdayOnly]
    # authentication_classes = [BasicAuthentication, TokenAuthentication]
    lookup_field = 'pk'
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['name']
    ordering_fields = ['name']

    def get(self, request, pk=None):
        if pk:
            category = get_object_or_404(Category, pk=pk)
            serializer = self.get_serializer(category)
            return Response(serializer.data)

        cache_key = f"course_list_user{request.user.id}_cat{request.GET.get('category', 'all')}"
        cache_data = cache.get(cache_key)
        if cache_data:
            return Response(cache_data)

        categories = self.get_queryset()
        page = self.paginate_queryset(categories)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            response = self.get_paginated_response(serializer.data)
            cache.set(cache_key, response.data, 60)
            return response

        serializer = self.get_serializer(categories, many=True)
        cache.set(cache_key, serializer.data, 60)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        cache.clear()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = self.get_serializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        cache.clear()
        return Response(serializer.data)

    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        cache.clear()
        return Response({'message': 'Category deleted'}, status=status.HTTP_204_NO_CONTENT)


@method_decorator(cache_page(60), name='get')
class CourseApiView(GenericAPIView):
    serializer_class = CourseModelSerializer
    queryset = Course.objects.select_related('course').all()
    permission_classes = [IsAuthenticated, IsWithInWorkingHours, WeekdayOnly]
    lookup_field = 'pk'
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['name']
    ordering_fields = ['name']

    def get_queryset(self):
        category = self.request.query_params.get('category')
        qs = Course.objects.select_related('category')
        return qs.filter(category_id=category) if category else qs

    def get(self, request, pk=None):
        if pk:
            course = get_object_or_404(Course, pk=pk)
            serializer = self.get_serializer(course)
            return Response(serializer.data)

        cache_key = f"course_list_user{request.user.id}_cat{request.GET.get('category', 'all')}"
        cache_data = cache.get(cache_key)
        if cache_data:
            return Response(cache_data, status=status.HTTP_200_OK)

        queryset = self.get_queryset()
        paginated_queryset = self.paginate_queryset(queryset)
        if paginated_queryset is not None:
            serializer = self.get_serializer(paginated_queryset, many=True)
            response = self.get_paginated_response(serializer.data)
            cache.set(cache_key, response.data, 60)
            return response

        serializer = self.get_serializer(queryset, many=True)
        cache.set(cache_key, serializer.data, 60)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        cache.clear()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        serializer = self.get_serializer(course, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        cache.clear()
        return Response(serializer.data)

    def delete(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        course.delete()
        cache.clear()
        return Response({'message': 'Course deleted'}, status=status.HTTP_204_NO_CONTENT)




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

        cache_key = f'teacher_list_{request.GET.get("teacher", "all")}'
        cache_data = cache.get(cache_key)
        if cache_data:
            return Response(cache_data, status=status.HTTP_200_OK)

        teachers = self.get_queryset()
        paginated_queryset = self.paginate_queryset(teachers)
        if paginated_queryset is not None:
            serializer = self.get_serializer(paginated_queryset, many=True)
            response = self.get_paginated_response(serializer.data)
            cache.set(cache_key, response.data, 60)
            return response

        serializer = self.get_serializer(teachers, many=True)
        cache.set(cache_key, serializer.data, 60)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        cache.clear()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        serializer = self.get_serializer(teacher, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        cache.clear()
        return Response(serializer.data)

    def delete(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        teacher.delete()
        cache.clear()
        return Response({'message': 'Teacher deleted'}, status=status.HTTP_204_NO_CONTENT)




class GroupApiView(GenericAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = [IsAuthenticated, IsWithInWorkingHours, WeekdayOnly]

    def get(self, request, pk=None):
        if pk:
            group = get_object_or_404(Group, pk=pk)
            serializer = self.get_serializer(group)
            return Response(serializer.data)
        cache_key = f'group_list_{request.GET.get("group", "all")}'
        cache_data = cache.get(cache_key)
        if cache_data:
            return Response(cache_data, status=status.HTTP_200_OK)

        groups = self.get_queryset()
        paginated_queryset = self.paginate_queryset(groups)
        if paginated_queryset is not None:
            serializer = self.get_serializer(groups, many=True)
            response = self.get_paginated_response(serializer.data)
            cache.set(cache_key, response.data, 60)
            return response

        serializer = self.get_serializer(groups, many=True)
        cache.set(cache_key, serializer.data, 60)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        cache.clear()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        group = get_object_or_404(Group, pk=pk)
        serializer = self.get_serializer(group, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        cache.clear()
        return Response(serializer.data)

    def delete(self, request, pk):
        group = get_object_or_404(Group, pk=pk)
        group.delete()
        cache.clear()
        return Response({'message': 'Group deleted'}, status=status.HTTP_204_NO_CONTENT)




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

        cache_key = f'module_list_{request.GET.get("module", "all")}'
        cache_data = cache.get(cache_key)
        if cache_data:
            return Response(cache_data, status=status.HTTP_200_OK)


        modules = self.get_queryset()
        paginated_queryset = self.paginate_queryset(modules)
        if paginated_queryset is not None:
            serializer = self.get_serializer(modules, many=True)
            response = self.get_paginated_response(serializer.data)
            cache.set(cache_key, response.data, 60)
            return response

        serializer = self.get_serializer(modules, many=True)
        cache.set(cache_key, serializer.data, 60)
        return Response(serializer.data)



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

        module_id = request.GET.get('module_id', 'all')
        cache_key = f'homework_list_{module_id}'
        cache_data = cache.get(cache_key)
        if cache_data:
            return Response(cache_data, status=status.HTTP_200_OK)

        homeworks = self.get_queryset()
        paginated_queryset = self.paginate_queryset(homeworks)
        if paginated_queryset is not None:
            serializer = self.get_serializer(paginated_queryset, many=True)
            cache.set(cache_key, serializer.data, 60)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(homeworks, many=True)
        cache.set(cache_key, serializer.data, 60)
        return Response(serializer.data)


class HomeworkDownloadApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        homework = get_object_or_404(Homework, pk=pk)
        file_handle = homework.file.open()
        response = FileResponse(file_handle, as_attachment=True, filename=homework.file.name.split('/')[-1])
        return response




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
        cache_key = f'video_list_{request.GET.get("video", "all")}'
        cache_data = cache.get(cache_key)
        if cache_data:
            return Response(cache_data, status=status.HTTP_200_OK)

        videos = self.get_queryset()
        paginated_queryset = self.paginate_queryset(videos)
        if paginated_queryset is not None:
            serializer = self.get_serializer(paginated_queryset, many=True)
            response = self.get_paginated_response(serializer.data)
            cache.set(cache_key, serializer.data, 60)
            return response

        serializer = self.get_serializer(videos, many=True)
        cache.set(cache_key, serializer.data, 60)
        return Response(serializer.data)



class StudentApiView(GenericAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.select_related('group').all()
    permission_classes = [IsAuthenticated, IsWithInWorkingHours, WeekdayOnly]
    lookup_field = 'pk'

    def get(self, request, pk=None):
        if pk:
            student = get_object_or_404(self.get_queryset(), pk=pk)
            serializer = self.get_serializer(student)
            return Response(serializer.data)

        cache_key = f'student_list_all{request.GET.get("student", "all")}'
        cache_data = cache.get(cache_key)
        if cache_data:
            return Response(cache_data, status=status.HTTP_200_OK)

        students = self.get_queryset()
        paginated_queryset = self.paginate_queryset(students)

        if paginated_queryset is not None:
            serializer = self.get_serializer(paginated_queryset, many=True)
            cache.set(cache_key, serializer.data, timeout=60)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(students, many=True)
        cache.set(cache_key, serializer.data, timeout=60)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        cache.clear()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        student = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(student, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        cache.clear()
        return Response(serializer.data)

    def delete(self, request, pk):
        student = get_object_or_404(self.get_queryset(), pk=pk)
        student.delete()

        cache.clear()
        return Response({'message': 'Student deleted'}, status=status.HTTP_204_NO_CONTENT)


class CountApiView(APIView):
    permission_classes = [IsAuthenticated, IsWithInWorkingHours, WeekdayOnly]

    def get(self, request):
        return Response({
            'total_categories': Category.objects.count(),
            'total_courses': Course.objects.count(),
            'total_teachers': Teacher.objects.count(),
            'total_groups': Group.objects.count(),
            'total_modules': Module.objects.count(),
            'total_homeworks': Homework.objects.count(),
            'total_videos': Video.objects.count(),
            'total_students': Student.objects.count()
        })


