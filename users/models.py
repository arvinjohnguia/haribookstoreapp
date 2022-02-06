from platform import architecture
from django.db import models
from datetime import datetime
import os, random
from django.utils import timezone
from django.utils.html import mark_safe


# Sa iba kinuha 'tong libraries sa baba nito, oks?
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

now = timezone.now()

def image_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxys1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    _now = datetime.now()
    
    return 'profile_pic/{year}-{month}-{imageid}-{basename}-{randomstring}{ext}'.format(imageid = instance, basename= basefilename, randomstring=randomstr, ext=file_extension, year=_now.strftime('%Y'), month=_now.strftime('%m'), day=_now.strftime('%d'))

class User(models.Model):
    user_fname = models.CharField(max_length=200, verbose_name='First Name')
    user_lname = models.CharField(max_length=200, verbose_name='Last Name')
    user_email = models.EmailField(unique=True, max_length=200, verbose_name='Email')
    
    class colleges(models.TextChoices):
        CAUP = 'CAUP', _('CAUP')
        Education = 'Education', _('Education')
        CET = 'CET', _('CET')
        CHASS = 'CHASS', _('CHASS')
        Medicine = 'Medicine', _('Medicine')
        Nursing = 'Nursing', _('Nursing')
        PT = 'PT', _('PT')
        CS = 'CS', _('CS')
        Law = 'Law', _('Law')
        NA = 'N/A', _('N/A')
    
    user_college = models.CharField(
        max_length=10, choices=colleges.choices,
        default=colleges.NA,
        verbose_name='College'
    )

    user_year = models.IntegerField(verbose_name='Year')
    user_course = models.CharField(max_length=200, verbose_name='Course')
    user_address = models.CharField(max_length=200, verbose_name='Address')
    user_gender = models.CharField(max_length=100, verbose_name='Gender')
    user_contactnumber = PhoneNumberField(verbose_name='Contact Number')
    user_birthdate = models.DateField(verbose_name='Birthdate')



    user_image = models.ImageField(upload_to=image_path, default='profile_pic/default_profile_image.jpg', verbose_name='Profile Picture')
    
    def image_tag(self):
        return mark_safe('<img src="/users/media/%s" width="50px" height="50px" />'%(self.user_image))

    def __str__(self):
        return self.user_email

def pro_image_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxys1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    _now = datetime.now()
    
    return 'inventory/{year}-{month}-{imageid}-{basename}-{randomstring}{ext}'.format(imageid = instance, basename= basefilename, randomstring=randomstr, ext=file_extension, year=_now.strftime('%Y'), month=_now.strftime('%m'), day=_now.strftime('%d'))

class Inventory(models.Model):
    pro_code = models.CharField(unique=True, max_length=10, verbose_name='Product Code')
    pro_name = models.CharField(max_length=200, verbose_name='Product Name')
    class categories(models.TextChoices):
        Filing = 'Filing Supplies', _('Filing Supplies')
        Paper = 'Paper Supplies', _('Paper Supplies')
        SchoolAndOffice = 'School and Office Essentials', _('School and Office Essentials')
        Writing  = 'Writing Supplies', _('Writing Supplies')
        Books = 'Books', _('Books')
        Unassigned = 'Unassigned', _('Unassigned')
    
    pro_category = models.CharField(
        max_length=100, choices=categories.choices,
        default=categories.Unassigned,
        verbose_name='Category'
    )

    pro_price= models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Price')
    pro_quantity = models.IntegerField(verbose_name='Stocks Left')
    pro_sold = models.IntegerField(blank=True, null=True, verbose_name='Quantity Sold')
    pro_totalsold = models.IntegerField(blank=True, null=True, verbose_name='Total Qty Sold')
    pro_totalsales = models.IntegerField(blank=True, null=True, verbose_name='Total Sale')



    pro_image = models.ImageField(upload_to=pro_image_path, default='supplies/placeholder.jpg', verbose_name='Product Image')
    
    def image_tag(self):
        return mark_safe('<img src="/users/media/%s" width="50px" height="50px" />'%(self.pro_image))

    def __str__(self):
        return self.pro_code