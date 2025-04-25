from django.contrib import admin
from django.utils.html import format_html

from erp.models import Category, Course, Student, Group, Teacher, Homework, Module, Video


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'student_code', 'group')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'course_id', 'teacher',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'username', 'image_tag')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width:50px; max-height:50px"/>'.format(obj.image.url))
        return '-'

    image_tag.short_description = 'Image'


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('module', 'overview', 'deadline')


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'group', 'date_passed')

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video', 'module')