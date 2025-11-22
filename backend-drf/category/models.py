from django.db import models

# Create your models here.
class Category(models.Model):
    category_name   = models.CharField(max_length=100)
    slug            = models.SlugField(unique=True)
    description     = models.TextField()
    category_image  = models.ImageField(upload_to='photos/categories/', blank=True, null=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.category_name