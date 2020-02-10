from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
# from django.db.models.signals import post_save

class CustomUser(AbstractUser):
    phone = models.PositiveIntegerField(blank=True, null=True, verbose_name= 'Номер телефона')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='Адрес')

    def get_absolute_profile_url(self):
        return reverse('accounts:edit_user', kwargs={'pk':self.pk})
# class Profile(CustomUser):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)




# def 
