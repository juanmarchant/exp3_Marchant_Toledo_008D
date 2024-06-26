from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def custom_upload_to_avatar(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    
    return 'profiles/avatar/' + filename


def custom_upload_head_image(instance, filename):
    try:
        old_instance = Product.objects.get(pk=instance.pk)
        old_instance.head_image.delete()
    except Product.DoesNotExist:
        pass

    return f'products/{instance.title}/{filename}'

class Product(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    title= models.CharField( max_length=50)
    description = models.TextField(blank=True, null=True)
    our_price = models.IntegerField(blank=True, null=True)
    head_image = models.ImageField(upload_to=custom_upload_head_image , null=True, blank=True)
    
    def __str__(self):
        return self.title



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to_avatar, null=True, blank=True)