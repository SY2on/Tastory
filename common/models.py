from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail

# Create your models here.


class User(AbstractUser):
    user_id = models.BigAutoField(primary_key=True)

    email = models.EmailField(
        max_length=254,
        unique=True
    )
    nickname = models.CharField(
        max_length=15,
        help_text=("필수기입. 15자 이하. 문자, 숫자, @/./+/-/_ 만 가능."),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.email


class Profile(models.Model):

    user_id = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    introduction = models.CharField(
        max_length=100,
        help_text=("100자 이하의 자기소개. 생략 가능합니다."),
        blank=True,
    )
    profile_img = models.ImageField(
        default='default.jpg',
        upload_to='profile_pics',
        null=True,
    )
