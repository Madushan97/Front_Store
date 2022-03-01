from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

def say_hello(request):

    # aal, get, filter
    # query_set = Product.objects.all()

    # if the query is empty then return will 0
    # None
    # product = Product.objects.filter(pk=1).first()

    # we are getting boolean value
    # exists = Product.objects.filter(pk=0).exists()

    # product = Product.objects.get(pk=1)

    # filtering data
    # queryset = Product.objects.filter(unit_price=20)
    # queryset = Product.objects.filter(unit_price__gt=20)
    # queryset = Product.objects.filter(unit_price__range=(20, 30))

    # cros relationship
    # queryset = Product.objects.filter(collection__id__range=(1,2,3))

    # finding coffee
    # startswith, endswith
    # queryset = Product.objects.filter(title__icontains='coffee')

    # for date
    # queryset = Product.objects.filter(last_update__year=2021)

    # getting all the data without description
    # queryset = Product.objects.filter(description__isnull=True)

    # adding multiple filters
    # products : inventory < 10 AND price < 20
    # queryset = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
    # queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
    # queryset = Product.objects.filter(Q(inventory__lt=10) | ~Q(unit_price__lt=20))

    # where inventory = price
    # queryset = Product.objects.filter(inventory = F('unit_price'))

    # sorting
    # queryset = Product.objects.order_by('-title')
    # return render(request, 'hello.html', {'name': 'Madushan', 'products': list(queryset)})
    # queryset = Product.objects.order_by('-title')
    # sorting multiple products
    # queryset = Product.objects.order_by('unit_price', '-title')
    # queryset = Product.objects.order_by('unit_price')[0]
    # queryset = Product.objects.earliest('unit_price')
    # descending
    # queryset = Product.objects.latest('unit_price')

    # limiting results
    # queryset = Product.objects.all()[:5]

    #filtering values
    # getting dictionaries as output
    # queryset = Product.objects.values('id', 'title', 'collection__title')

    # getting tuples as output
    queryset = Product.objects.values_list('id', 'title', 'collection__title')
    return render(request, 'hello.html', {'name': 'Madushan', 'products': list(queryset)})     
   
