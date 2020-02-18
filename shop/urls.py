from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('cart/', views.cart_list, name='cart_list'),
    path('<int:pk>', views.product_detail, name='product_detail'),
    path('custom/<int:pk>', views.custom_purchase_detail, name='custom_detail'),
    path('<int:pk>/add/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:pk>', views.delete_from_cart, name = 'delete_from_cart'),
    path('about/', views.about, name='about'),
    path('done/', views.done_purchases, name='done_purchases'),
    path('<str:product_type>', views.product_list, name='product_type'),
    # path('upload/', views.upload, name='upload'),
    path('custom_create/', views.custom_create, name='custom_create'),
    path('like/<int:pk>', views.like, name='like'),
    path('accept/<int:pk>', views.accept, name='accept'),
    
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_roor = settings.MEDIA_ROOT)