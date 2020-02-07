from django.db import models
from django.urls import reverse
from django.utils import timezone
from mysite import settings

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='awaiting')

class Product(models.Model):
    STATUS_CHOISES = (
        ("awaiting", 'Ждет ответа'),
        ('confirmed', 'Подтвержден'),
        ('done', 'Выполнен'),
    )
    TYPE_CHOISES = (
        ('figure', "Фигурка"),
        ('earring', "Серьги"),
        ('necklace', "Кулон"),
    )
    name = models.CharField(max_length=255)
    product_type = models.CharField(max_length=10, choices=TYPE_CHOISES)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOISES, null=True, blank=True)
    # clients = models.ManyToManyField(settings.AUTH_USER_MODEL, null=True, blank=True)
    rate = models.PositiveIntegerField(null=True, blank=True)
    # cart = PublishedManager()
    objects = models.Manager()

    class Meta:
        ordering = ('-price',)

    # def get_absolute_url(self):
    #     return reverse('shop:post_detail', args=[self.publish.year, 
    #                                             self.publish.month, 
    #                                             self.publish.day, 
    #                                             self.slug])

    def __str__(self):
        return self.name