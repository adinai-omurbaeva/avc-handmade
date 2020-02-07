from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('cart/', views.cart_list, name='cart_list'),
    path('<int:pk>', views.product_detail, name='product_detail'),
]