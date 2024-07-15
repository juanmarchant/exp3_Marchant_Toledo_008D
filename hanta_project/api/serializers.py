import requests
from django.core.files.base import ContentFile
from rest_framework import serializers
from core.models import Product

class ProductSerializer(serializers.ModelSerializer):
    head_image_url = serializers.URLField(write_only=True, required=False)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'our_price', 'head_image', 'head_image_url']

    def create(self, validated_data):
        head_image_url = validated_data.pop('head_image_url', None)
        product = super().create(validated_data)

        if head_image_url:
            response = requests.get(head_image_url)
            if response.status_code == 200:
                file_name = head_image_url.split("/")[-1]
                product.head_image.save(file_name, ContentFile(response.content), save=True)

        return product

    # def create(self, validated_data):
    #     product = Product()
    #     product.title = validated_data.get('title')
    #     product.description= validated_data.get('description')
    #     product.our_price = validated_data.get('our_price')
    #     product.head_image = validated_data.get('head_image')
    #     return product
    
    # def validate_title(self, validated_data):
    #     products = Product.objects.filter(title= validated_data)
    #     if len(products)!= 0:
    #         raise serializers.ValidationError('The product already exist, try with another title')
    #     else:
    #         return validated_data
# id = models.CharField(primary_key=True, max_length=10)
# title= models.CharField( max_length=50)
# description = models.TextField(blank=True, null=True)
# our_price = models.IntegerField(blank=True, null=True)
# head_image = models.ImageField(upload_to=custom_upload_head_image , null=True, blank=True)