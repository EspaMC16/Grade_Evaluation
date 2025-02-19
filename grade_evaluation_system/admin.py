from django.contrib import admin

from .models import Subject, Instructor, Course, Grade


admin.site.register(Subject)
admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Grade)
