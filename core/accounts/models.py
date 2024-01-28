from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from .manager import UserManager




class CustomUser(AbstractUser,PermissionsMixin):
    
    phone_number = models.CharField(max_length = 100, unique = True)
    user_bio = models.CharField(max_length = 50)
    email = models.EmailField(unique = True)
    username = None
    user_profile_image = models.ImageField(upload_to="profile")
    
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()

    
    
    
    
    