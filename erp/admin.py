from django.contrib import admin

from erp.models import Category, Course, Student, Group, Teacher, Homework, Module



# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Teacher)
admin.site.register(Homework)
admin.site.register(Module)
# admin.site.register(Video)