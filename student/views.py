from django.shortcuts import render, redirect
from student.models import BroadwayStudent, StudentClass
from student.forms import StudentClassForm
# Create your views here.

def fetch_student(request):
        a=BroadwayStudent.objects.all()
       
        #return HttpResponse(a)
        context = {
                "data":a
        }
        return render(request, 'student/index.html', context)


def featch_class(request):
        b=StudentClass.objects.all()
       
        #return HttpResponse(a)
        context = {
                "data":b
        }
        return render(request, 'class/index.html', context)

def create_class(request):
       form = StudentClassForm
       if request.method=='POST':
               form= StudentClassForm(request.POST)
               if form.is_valid():
                       form.save()
                       return redirect('/')
               else:
                       print(form.errors)


       context = {
        "form": form
        }
       
       return render(request, 'class/create.html', context)