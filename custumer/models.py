from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin, AbstractBaseUser,BaseUserManager

from django.utils import timezone

# Create your models here.

class CustumerAccountManager(BaseUserManager):
    def create_user(self, email, user_name,first_name,password, **other_fields):
        if not email:
            raise ValueError("you must provide a email address")
        email=self.normalize_email(email)
        user=self.model(email=email,user_name=user_name,first_name=first_name,**other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name,first_name, **other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)
        if other_fields.get('is_staff') is not True:
            raise ValueError('superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('superuser must be assigned to is_superuser=True.')
        
        return self.create_user(email, user_name,first_name,**other_fields)
    
    
class NewUser(AbstractBaseUser,PermissionsMixin):
    user_name=models.CharField(max_length=30,unique=True)
    first_name=models.CharField(max_length=30)
    start_date=models.DateTimeField(default=timezone.now)
    email=models.EmailField(max_length=255,unique=True)
    adresse=models.CharField(max_length=300, blank=True, null=True)
    city=models.CharField(max_length=30)
    about_me=models.TextField(max_length=500, blank=True, null=True)
    profile_image=models.ImageField(null=True)
    is_active=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)

    objects=CustumerAccountManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['user_name','first_name']
    
    def __str__(self):
        return self.user_name
    
