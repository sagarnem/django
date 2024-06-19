from django.urls import path
from student.views import fetch_student, featch_class, create_class
urlpatterns = [
        path('', fetch_student, name="fetch-student"),
        path('class', featch_class, name="class-list"),
        path('class/form', create_class, name='create-list')

]