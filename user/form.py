from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Createuser(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'

