from django.shortcuts import render , redirect , get_object_or_404
from django.shortcuts import render, redirect
from .models import Product , Review , Bidding
from django.contrib.auth.decorators import login_required

def product_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        brand = request.POST.get('brand')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        description = request.POST.get('description')

        product = Product(
            user=request.user,
            name=name,
            brand=brand,
            price=price,
            image=image,
            image1=image1,
            image2=image2,
            image3=image3,
            description=description,
        )
        product.save()
        return redirect('home')  

    return render(request, 'product_form.html')



def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    reviews = product.reviews.all()
    bids = product.bids.all()   # ordered if you used Meta ordering

    highest_bid = bids.first()  # top bid (None if no bids)

    return render(request, "product_detail.html", {
        "product": product,
        "reviews": reviews,
        "bids": bids,
        "highest_bid": highest_bid,
    })



@login_required
def my_listing(request):
    products = Product.objects.filter(user=request.user)
    return render(request, 'my_listing.html', {"products": products})


@login_required
def product_edit(request, id):
    product = get_object_or_404(Product, id=id) 

    if request.method == "POST":
        product.name = request.POST.get('name') 
        product.brand = request.POST.get('brand')
        product.price = request.POST.get('price')
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        product.description = request.POST.get('description')
        product.save()
        return redirect('my_listing')

    return render(request, 'product_edit.html', {"product": product})

@login_required
def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('my_listing')



@login_required
def product_review(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        name = request.POST["name"]
        rating = request.POST["rating"]
        comment = request.POST["comment"]

        Review.objects.create(
            user=request.user,
            product=product,
            name=name,
            rating=rating,
            comment=comment
        )
        return redirect("product_detail", id=product.id)  # back to detail page

    return render(request, "product_review.html", {"product": product})


@login_required
def product_bidding(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        bid_amount = request.POST.get('bid_amount')

        Bidding.objects.create(
            bid_amount=bid_amount,
            product=product,
            user=request.user,
        )

        return redirect('product_bidding', id=product.id)
    bids = product.bids.all().order_by('-bid_amount')
    return render(request, 'product_bidding.html', {
        "product": product,
        "bids": bids,
    })

