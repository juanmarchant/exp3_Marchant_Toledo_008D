

from django import forms 

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import PasswordInput
from .models import Product, Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']

class ProductForm(forms.ModelForm):
    class Meta: 
        model=Product
        fields=['id', 'title', 'description', 'our_price','head_image']
        labels={
            'id': 'Id ',
            'title': 'Title',
            'description': 'Description',
            'our_price': 'Price',
            'head_image': 'Image',
        }
        widgets={
            'id': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Add the id',
                    'id':'id'
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Add the title of the game',
                    'id':'title'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Add the description',
                    'id':'description'
                }
            ),
            'our_price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Add the price',
                    'id':'price'
                }
            ),
            'head_image': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id':'image'
                }
            )
        }
class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name' ,'username', 'email', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control ',
                }
            ),
            
        }

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = PasswordInput(attrs={'class': 'form-control'})


