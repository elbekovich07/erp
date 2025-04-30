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


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    student_code = serializers.CharField(read_only=True)
    group_name = GroupSerializer(read_only=True)

    class Meta:
        model = Student
        fields = [
            'id', 'first_name', 'last_name', 'gender',
            'phone_number', 'password', 'image',
            'student_code', 'group', 'group_name'
        ]
        extra_kwargs = {
            'password': {'write_only': False}
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




class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        exclude = ('is_given',)


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'

    def save(self, **kwargs):
        homework = super().save(**kwargs)
        module = homework.module
        module.is_active = True
        module.save()
        return homework

class VideoSerializer(serializers.ModelSerializer):
    formatted_size = serializers.ReadOnlyField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = ['id', 'title', 'file', 'created_at', 'module', 'status', 'formatted_size']

    def get_status(self, obj):
        return obj.status
