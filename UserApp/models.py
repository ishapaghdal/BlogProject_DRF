from django.db import models
from django.core.validators import RegexValidator
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import AbstractUser
from .managers import UserManager

class User(AbstractUser):
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=50,unique=True)
    name = models.CharField(max_length=50,null=True,blank=True)
    bio = models.TextField(blank=True)
    picture = models.CharField(max_length=200,null=True)
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must be in the '9999999999' format.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = UserManager()

    def __str__(self):
        return self.username
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }
