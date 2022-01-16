from django.contrib import admin

from .models import Employee,Subject,Student
# Register your models here.

admin.site.register(Employee)
admin.site.register(Subject)
admin.site.register(Student)