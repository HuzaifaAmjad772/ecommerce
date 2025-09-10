from django.shortcuts import render , redirect , get_object_or_404
from . models import Product

from django.shortcuts import render, redirect
from .models import Product 

def product_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        brand = request.POST.get('brand')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        description = request.POST.get('description')

        product = Product(
            name=name,
            brand=brand,
            price=price,
            image=image,
            description=description,
        )
        product.save()
        return redirect('home')  

    return render(request, 'product_form.html')



def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {"product": product})



def my_listing(request):
    products = Product.objects.filter(user=request.user)
    return render(request, 'my_listing.html', {"products": products})