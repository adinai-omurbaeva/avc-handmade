from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Purchase, Comment, CustomPurchase
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm, CartCreationForm, CustomPurchaseForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect

def product_list(request, product_type=None):
    if product_type==None:
        object_list = Product.objects.all().order_by('-likes_number')
    else:
        object_list = Product.objects.filter(product_type=product_type).order_by('-likes_number')
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
    
    is_liked = False
    if product.likes.filter(id=request.user.id).exists():
        is_liked = True

    comments = product.comments.filter(active=True)
    new_comment = None
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
                                           'comment_form': comment_form
                                           })
@login_required
def custom_purchase_detail(request, pk):
    custom_purchase = get_object_or_404(CustomPurchase, pk=pk)
    images = [custom_purchase.image1, custom_purchase.image2, custom_purchase.image3]

    while 'no-image.jpg' in images:
        images.remove('no-image.jpg')
    if bool(images)==False:
        images = [custom_purchase.image1,]
    return render(request, 'custom_purchase_detail.html', {'custom_purchase': custom_purchase,
                                                            'images':images})

@login_required
def cart_list(request):
    carts = Purchase.objects.filter(Q(customer=request.user, status='awaiting')|Q(customer=request.user, status='confirmed')).order_by('status')
    total = 0
    custom = CustomPurchase.objects.filter(customer=request.user)
    is_empty = bool(carts)
    is_anycustom = bool(custom)
    for i in carts:
        total += i.cost
    return render(request, 'cart.html', {'carts': carts,
                                        'total':total,
                                        'is_empty':is_empty,
                                        'custom':custom,
                                        'is_anycustom':is_anycustom})

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
        form = CustomPurchaseForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            new_cart = form.save(commit=False)
            print(new_cart)
            new_cart.customer = request.user
            new_cart.save()
            messages.success(request, 'It has successfully added')
            return redirect('shop:custom_detail', new_cart.pk)
    else:
        form = CustomPurchaseForm(data=request.GET)
    return render(request, 'create_custom.html', {'form':form})

@login_required
def custom_edit(request, pk):
    cp = get_object_or_404(CustomPurchase, pk=pk)
    if request.method=='POST':
        form = CustomPurchaseForm(request.POST, instance=cp)
        if form.is_valid():
            cp=form.save(commit=False)   
            cp.save()
            return redirect('shop:custom_detail', pk)
    else:
        form = CustomPurchaseForm(request.POST, instance=cp)
    return render(request, 'edit_custom.html', {'form':form})

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
            return redirect('shop:product_list')
    else:
        form = CartCreationForm(data=request.GET)
    return render(request, 'add_to_cart.html', {'form':form})

@login_required
def delete_custom_purchase(request, pk):
    purchase = CustomPurchase.objects.get(pk=pk)
    if purchase.status=='awaiting':
        purchase.delete()
        return redirect('shop:cart_list')
    return render(request, 'error_page.html')

@login_required
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
def like(request, pk):
    product = get_object_or_404(Product, pk=pk)
    is_liked = False
    if product.likes.filter(id=request.user.id).exists():
        product.likes.remove(request.user)
        product.likes_number-=1
        product.save()
        is_liked = False
    else:
        product.likes.add(request.user)
        product.likes_number+=1
        product.save()
        is_liked = True
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def accept(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)
    purchase.status='confirmed'
    purchase.save()
    return redirect('shop:cart_list')

@login_required
def custom_accept(request, pk):
    purchase = get_object_or_404(CustomPurchase, pk=pk)
    purchase.status='confirmed'
    purchase.save()
    return redirect('shop:cart_list')