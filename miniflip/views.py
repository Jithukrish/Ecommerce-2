from django.shortcuts import render,get_object_or_404
from django.http import Http404,HttpRequest,HttpResponse
from .models import Product

def index(request):

    feactured_product=Product.objects.order_by( 'priority')[:4]
    latest_product=Product.objects.order_by( '-id')[:4]
    context={
        "feactured_product":feactured_product,
        "latest_product":latest_product
    }
    print(context)
    return render(request,'blank_layout.html',context)

def list_products(request):
    product_list=Product.objects.all()
    context={'products':product_list}
    return render(request,'products.html',context)


def detail_description(request,pk):
    product=Product.objects.get(pk=pk)
    # product = get_object_or_404(Product, pk=pk)
    context={"product":product}
    return render(request,'product_details.html',context)

def detail_products(request,pk):
    product=Product.objects.get(pk=pk)
    # product = get_object_or_404(Product, pk=pk)
    context={"product":product}
    return render(request,'product_detail.html',context)
