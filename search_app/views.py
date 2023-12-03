from django.shortcuts import render
from shop.models import Product
from django.db.models import Q


def search_results(request):
    query = request.POST['search_query']

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        products = Product.objects.all()

    context = {
        'products': products,
        'query': query,
    }

    return render(request, 'search_results.html', context)


