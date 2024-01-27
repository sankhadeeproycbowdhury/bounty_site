from django.contrib.auth.base_user import BaseUserManager

# Abhijeet , abhijeet both are same but in case of email  thet signify differnt user
# so we need to normalize email....!!!!

class UserManager(BaseUserManager):
    
    def create_user(self , phone_number , password = None ,  **extra_fields):
        if not phone_number:
            raise ValueError("Phone Number Missing!!")
        
        extra_fields['email'] = self.normalize_email(extra_fields['email'])
        user = self.model(phone_number = phone_number,  **extra_fields)
        user.set_password(password)
        user.save(using = self.db)
        
        return user
    
    
    def create_superuser(self , phone_number , password = None ,  **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_active', True)
        
        return self.create_user( phone_number, password, **extra_fields)
    
    
        