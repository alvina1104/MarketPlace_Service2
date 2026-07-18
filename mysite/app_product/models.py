from django.db import models

class Category(models.Model):
    category_image = models.ImageField(upload_to='category_images')
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    product_name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    article = models.PositiveIntegerField(unique=True)
    is_official = models.BooleanField(default=False)
    video = models.FileField(upload_to='product_videos', null=True,blank=True)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    owner = models.IntegerField()

    def __str__(self):
        return self.product_name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    product_image = models.ImageField(upload_to='product_image')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.product_name} - Photo"