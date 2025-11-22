from django.contrib import admin
from .models import Category

# this class is used to auto populate the slug field based on category_name field
class CategoryAdmin(admin.ModelAdmin):
    # this will auto populate the slug field
    prepopulated_fields = {'slug': ('category_name',)}
    
    # this will display the following fields in admin panel
    list_display = ('category_name', 'slug', 'description', 'category_image')


# Register your models here.
admin.site.register(Category, CategoryAdmin)