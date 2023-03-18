from django.db import models

class Product(models.Model):
    en_title = models.CharField('EN Title',max_length=300, null=True)
    ru_title = models.CharField('RU Title',max_length=300, null=True)
    az_title = models.CharField('AZ Title',max_length=300, null=True)
    amount = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField('Price',max_digits=6, decimal_places=2)
    en_compound = models.TextField('EN Compound')
    az_compound = models.TextField('AZ Compound')
    ru_compound = models.TextField('RU Compound')
    image = models.ImageField('Image',upload_to='images/', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, db_index=True, related_name='products', null=False, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"{self.en_title}"
    

class Category(models.Model):
    en_title = models.CharField('EN Title',max_length=300, null=True)
    ru_title = models.CharField('RU Title',max_length=300, null=True)
    az_title = models.CharField('AZ Title',max_length=300, null=True)
    image = models.ImageField('Image',upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f"{self.en_title}"