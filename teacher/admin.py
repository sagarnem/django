from django.contrib import admin
from teacher.models import BroadwayTeacher

@admin.register(BroadwayTeacher)
class BroadwayTeacherAdmin(admin.ModelAdmin):
    list_display=['id','name','address','phone']
    search_fields=['name','address']
