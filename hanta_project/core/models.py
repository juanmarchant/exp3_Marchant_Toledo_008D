from django.db import models

# Create your models here.




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
    

# "ID": "251570",
# "GAMES": "7 DAYS TO DIE",
# "OUR_PRICE": "$14.28",
# "STEAM_PRICE": "$12,000.00",
# "CHILE_PRICE_USD": "$12.18",
# "CHILE_PRICE ": "$12000",
# "VALIDATE": "FALSE",
# "DESCRIPTION": "7 Days to Die is an open-world game that is a unique combination of first-person shooter, survival horror, tower defense, and role-playing games. Play the definitive zombie survival sandbox RPG that came first. Navezgane awaits!",
# "HEAD_IMAGE": "https://cdn.akamai.steamstatic.com/steam/apps/251570/header.jpg?t=1702072288",
# "IMAGE_1": "https://cdn.akamai.steamstatic.com/steam/apps/251570/ss_66ab2c612cb28b4b61974bcb3380a69274c4c127.1920x1080.jpg?t=1702072288",
# "IMAGE_2": "https://cdn.akamai.steamstatic.com/steam/apps/251570/ss_573fbb7a06c0b269de2c1e562b0129412f42792f.1920x1080.jpg?t=1702072288",
# "IMAGE_3": "https://cdn.akamai.steamstatic.com/steam/apps/251570/ss_cb37f3a4226d16fbb0e4681605ef592acba3077f.1920x1080.jpg?t=1702072288",
# "IMAGE_4": "https://cdn.akamai.steamstatic.com/steam/apps/251570/ss_fab3d39d4fdcab63df04a5e7bb69b5c0f81a0896.1920x1080.jpg?t=1702072288"