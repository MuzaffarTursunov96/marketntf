from distutils import extension
from distutils.command.upload import upload
from email.policy import default
import os
import jsonfield
import string
import random
from datetime import datetime
from pyexpat import model
from unicodedata import decimal
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage(location='/media/uploads')

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, username, password):
        if not email:
            raise ValueError('User must have an email')
        if not username:
            raise ValueError('User must have an username')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, username, password):
        user  = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username
        )
        user.is_admin     = True
        user.is_staff     = True
        user.is_superuser = True
        user.save( using = self._db )
        return user


class User(AbstractBaseUser):
    avatar          = models.ImageField(upload_to = f'user{os.sep}',default='images/example.jpg',blank=True,null=True)
    biograph        = models.TextField(default = '')
    email           = models.EmailField(verbose_name = 'Email', max_length = 60, unique = True)
    username        = models.CharField(max_length = 50, unique = True)
    date_joined     = models.DateTimeField(verbose_name = 'date joined', auto_now_add = True)
    is_admin        = models.BooleanField(default = False)
    is_staff        = models.BooleanField(default = False)
    is_superuser    = models.BooleanField(default = False)
    last_login      = models.DateTimeField(default=datetime.now)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username']

    objects         = UserManager()

    def __str__(self):
        return f'{self.username} {self.email}'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Projects(models.Model):
  name = models.CharField(max_length=255)
  slug = models.CharField(max_length=255)
  liked = models.BooleanField(default=False)
  likes = models.IntegerField(default=0)
  description = models.TextField(default="")
  image = models.ImageField(upload_to='images/',blank=True,null=True)
  price = models.FloatField(default=0)
  time_left = models.CharField(max_length=50,default=str(datetime.now()))
  creator = models.ForeignKey(User, on_delete=models.PROTECT)
  collection = models.ForeignKey('Collection',on_delete=models.PROTECT,blank=True,null=True)
  biddings = jsonfield.JSONField(default=[])
  bought = models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class Collection(models.Model):
  name =models.CharField(max_length = 255)
  avatar = models.ImageField(upload_to = 'collections/',blank=True,null=True ,default='images/example.jpg')
  def __str__(self):
    return self.name

class History(models.Model):
  project = models.ForeignKey(Projects, on_delete = models.PROTECT)
  date = models.DateTimeField(default=datetime.now, blank=True,null=True)
  price =models.FloatField(default=0)

class Image(models.Model):
  name = models.ImageField(upload_to ='images/')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def __str__(self):
    return str(self.name)

class Wishlist(models.Model):
  user = models.ForeignKey(User,on_delete=models.PROTECT)
  project = models.ForeignKey(Projects,on_delete=models.PROTECT)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
