from django.urls import path
from student.views import fetch_student, featch_class
urlpatterns = [
        path('', fetch_student, name="fetch-student"),
        path('class', featch_class, name="class-list")
]