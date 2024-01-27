from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    
    def create_user(self , phone_number , password = None , **extra_fields):
        if not phone_number:
            raise ValueError("Phone Number Missing!!")
        
        #extra_fields['email'] = self.normalize_email(extra_fields['email'])
        user = self.model(phone_number = phone_number,  **extra_fields)
        user.set_password(password)
        user.save(using = self.db)
        
        return user
    
    
    def create_superuser(self , phone_number , password = None ,  **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        #extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_active', True)
        
        return self.create_user( phone_number, password, **extra_fields)
    

class CustomUser(AbstractUser,PermissionsMixin):
    
    phone_number = models.CharField(max_length = 100, unique = True)
    user_bio = models.CharField(max_length = 50)
    email = models.EmailField(unique = True)
    username = None
    user_profile_image = models.ImageField(upload_to="profile")

    objects = UserManager()

    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    
    
    