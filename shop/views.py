from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Purchase, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm

def product_list(request):
    object_list = Product.objects.all().order_by('-price')
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

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comments = product.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.name = request.user
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'product_detail.html', {'product': product,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

def cart_list(request):
    carts = Purchase.objects.filter(customer=request.user)
    total = 0
    for i in carts:
        total += i.cost
    # price = Purchase.cost.filter(customer = request.user)
    return render(request, 'cart.html', {'carts': carts,
                                        'total':total})

