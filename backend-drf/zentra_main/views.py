from django.shortcuts import render
from store.models import Product


def home(request):
    products = Product.objects.all().filter(is_available = True)
    # we will get all the info of products in product 
    
    context = {
        'products': products
    }
    return render(request, 'home.html', context)