from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager



class MyaccountManager(BaseUserManager):
    def create_user(self,email, username, password=None):
        if not email:
            raise ValueError("user must have an email address")
        if not username:
            raise ValueError("Users must have a username address")
        user=self.model(
            email=self.normalize_email(email),
            username=username.lower()
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,username,password):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username.lower(),
            password=password
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email=models.EmailField(verbose_name='email',max_length=60,unique=True)
    username=models.CharField(max_length=30)
    date_joined=models.DateTimeField(verbose_name='date joined',auto_now_add=True)
    last_login=models.DateTimeField(verbose_name='last login',auto_now_add=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    objects = MyaccountManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    
    def __str__(self):
        return self.username
    def has_perm(self, perm ,obj=None):
        return self.is_admin
    def has_module_perms(self,mysite):
        return self.is_admin
        