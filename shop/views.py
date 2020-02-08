from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Purchase, Comment, Like
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm, CartCreationForm, CustomPurchaseForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

def product_list(request, product_type=None):
    if product_type==None:
        object_list = Product.objects.all().order_by('-price')
    else:
        object_list = Product.objects.filter(product_type=product_type).order_by('-price')
    paginator = Paginator(object_list, 6)
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
    like = Like.objects.filter(like='like', product=product)
    dislike = Like.objects.filter(like='dislike',product=product)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.name = request.user
            new_comment.save()
            comment_form=CommentForm()
    else:
        comment_form = CommentForm()
    return render(request, 'product_detail.html', {'product': product,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'like':like,
                                           'dislike':dislike})
@login_required
def cart_list(request):
    carts = Purchase.objects.filter(Q(customer=request.user, status='awaiting')|Q(customer=request.user, status='confirmed'))
    total = 0
    is_empty = bool(carts)
    for i in carts:
        total += i.cost
    return render(request, 'cart.html', {'carts': carts,
                                        'total':total,
                                        'is_empty':is_empty})

def about(request):
    return render(request, 'index.html')

def upload(request):
    if request.method == 'POST':
        uploaded_file= request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
    return render(request, 'upload.html', locals())

@login_required
def custom_create(request):
    if request.method == 'POST':
        form = CustomPurchaseForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            new_cart = form.save(commit=False)
            new_cart.customer = request.user
            new_cart.save()
            messages.success(request, 'It has successfully added')
            return redirect('shop:product_list')
    else:
        form = CustomPurchaseForm(data=request.GET, files=request.FILES)
        return render(request, 'create_custom.html', {'form':form})

@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = CartCreationForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_cart = form.save(commit=False)
            new_cart.customer = request.user
            new_cart.product = product
            new_cart.save()
            messages.success(request, 'Added')
            return redirect('shop:product_list')
    else:
        form = CartCreationForm(data=request.GET)
        return render(request, 'add_to_cart.html', {'form':form})

def delete_from_cart(request, pk):
    purchase = Purchase.objects.get(pk=pk)
    if purchase.status=='awaiting':
        purchase.delete()
        return redirect('shop:cart_list')
    return render(request, 'error_page.html')

@login_required
def done_purchases(request):
    done = Purchase.objects.filter(customer=request.user, status='done')
    return render(request, 'done_purchases.html', {'done': done})

@login_required
def like(request, pk, like_type):
    product = get_object_or_404(Product, pk=pk)
    old_like=Like.objects.filter(product=product, customer=request.user)
    if bool(old_like):
        if like_type!=old_like[0].like:
            old_like.delete()
            new_like=Like()
            new_like.customer=request.user
            new_like.product = product
            new_like.like=like_type
            new_like.save()
    else:
        new_like=Like()
        new_like.customer=request.user
        new_like.product = product
        new_like.like=like_type
        new_like.save()
    return redirect('shop:product_list')

