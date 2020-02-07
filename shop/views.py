from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def product_list(request):
    object_list = Product.objects.all().order_by('-price')
    # object_list = Post.published.filter(author=request.user)
    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    
    return render(request, 'list.html', {'page': page, 
                                        'products': products})
