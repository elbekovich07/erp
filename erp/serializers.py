from rest_framework import serializers

from .models import Category, Course, Module, Group, Homework, Video, Student, Teacher


class CourseModelSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    courses = CourseModelSerializer(many=True, read_only=True)
    slug = serializers.SlugField(read_only=True)
    course_count = serializers.SerializerMethodField(method_name='get_course_count')

    def get_course_count(self, instance):
        return instance.courses.count()


    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'courses', 'course_count']


class StudentSerializer(serializers.ModelSerializer):
    student_code = serializers.CharField(read_only=True)
    group_name = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = [
            'id', 'first_name', 'last_name', 'gender',
            'phone_number', 'password', 'image',
            'student_code', 'group', 'group_name'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def get_group_name(self, obj):
        return obj.group.name if obj.group else None

    def create(self, validated_data):
        validated_data.pop('user', None)
        return super().create(validated_data)


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


