


from django.contrib.auth.forms import userCreationForm
from django.contrib.auth.models import User

class RegisterUserForm(userCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name' 'username', 'email', 'password1', 'password2']