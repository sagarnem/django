from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def user_list(request):
    user = User.objects.all()
    context = {
        "user": user
    }

    return render (request, 'user/index.html', context)

def create_user(request):
    form = UserCreationForm()
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user')
        else:
            print(form.errors)

    context = {
                "form": form
            }

    return render(request, 'user/create.html', context)