from django.db import models

# Create your models here.
class Category(models.Model):

    name = models.CharField('Category name', max_length=60)

    def __str__(self):
        return self.name
    
class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='abc')
    name = models.CharField('Product name', max_length=80)
    img = models.ImageField('Product image', upload_to='prod_images')
    price = models.PositiveIntegerField('product price')

    def __str__(self):
        return self.name