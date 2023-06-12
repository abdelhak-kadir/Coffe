from django.shortcuts import get_object_or_404, render
from .models import Product
# Create your views here.


def products(request):  # request : refers to an object that represents an HTTP request that is received by a view function
    pro = Product.objects.all()
    name = None
    desc = None
    pfrom = None
    pto = None
    cs = None  # case sensitive
    if 'cs' in request.GET:
        cs = request.GET['cs']
        if cs:
            cs = 'off'

    if 'searchname' in request.GET:
        name = request.GET['searchname']
        if name:
            if cs == 'on':
                # with sensitive   filtr :allows you to retrieve a subset of objects from the database based on specific criteria
                pro = pro.filter(name__contains=name)
            else:
                pro = pro.filter(name__icontains=name)  # without sensitive
    if 'searchdesc' in request.GET:
        desc = request.GET['searchdesc']
        if desc:
            if cs == 'on':
                pro = pro.filter(desciption__contains=desc)
            else:
                pro = pro.filter(desciption__icontains=desc)
    if 'searchpricefrom' in request.GET and 'searchpriceto' in request.GET:
        pfrom = request.GET['searchpricefrom']
        pto = request.GET['searchpriceto']
        if pfrom and pto:
            if pfrom.isdigit() and pto.isdigit():
                # gte : great than equal to \ lte : less than
                pro = pro.filter(price__gte=pfrom, price__lte=pto)
    context = {
        'products': pro
    }
    return render(request, 'products/products.html', context)


def product(request, pro_id):
    contexte = {
        'pro': get_object_or_404(Product, pk=pro_id)
    }
    return render(request, 'products/product.html', contexte)


def search(request):
    return render(request, 'products/search.html')

# render : render templates with context data and return HTTP responses
