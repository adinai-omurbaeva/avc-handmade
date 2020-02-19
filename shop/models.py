from django.db import models
from django.urls import reverse
from django.utils import timezone
from mysite import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class Product(models.Model):
    TYPE_CHOISES = (
        ('badge', "Значок"),
        ('earring', "Серьги"),
        ('necklace', "Кулон"),
    )
    name = models.CharField(max_length=255)
    product_type = models.CharField(max_length=10, choices=TYPE_CHOISES)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='static/images', blank=True)
    # likes = models.IntegerField(default=0)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', blank=True)
    likes_number = models.IntegerField(default=0)
    # status = models.CharField(max_length=10, choices=STATUS_CHOISES, null=True, blank=True)
    # clients = models.ManyToManyField(settings.AUTH_USER_MODEL, null=True, blank=True)
    # rate = models.PositiveIntegerField(null=True, blank=True)
    # cart = PublishedManager()
    objects = models.Manager()

    class Meta:
        ordering = ('-price',)
        
    def __str__(self):
        return self.name



class Purchase(models.Model):
    STATUS_CHOISES = (
        ("awaiting", 'В обработке'),
        ('confirmed', 'Подтвержден'),
        ('done', 'Готов'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOISES, default='awaiting')
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='basket', on_delete='CASCADE')
    product = models.ForeignKey(Product, related_name='+', on_delete='CASCADE')
    date = models.DateTimeField(auto_now_add=True)
    count = models.PositiveSmallIntegerField(verbose_name='Количество')

    @property
    def cost(self):
        return self.product.price * self.count


class CustomPurchase(models.Model):
    STATUS_CHOISES = (
        ("awaiting", 'В обработке'),
        ('confirmed', 'Подтвержден'),
        ('done', 'Готов'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOISES, default='awaiting', blank=True, null=True)
    image1 = models.ImageField(upload_to='static/images', verbose_name='Изображение 1', blank=True, default='no-image.jpg')
    image2 = models.ImageField(upload_to='static/images', blank=True, verbose_name='Изображение 2', default='no-image.jpg')
    image3 = models.ImageField(upload_to='static/images', blank=True, verbose_name='Изображение 3', default='no-image.jpg')
    description = models.TextField(verbose_name='Описание')
    size = models.PositiveIntegerField(verbose_name='Размер')
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete='CASCADE')


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField()
    body = models.TextField(verbose_name='Текст')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'comment by {} on {}'.format(self.name, self.product)