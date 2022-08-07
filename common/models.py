from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.contrib.auth.validators import UnicodeUsernameValidator
# Create your models here.


class User(AbstractUser):
    user_id = models.BigAutoField(primary_key=True)

    email = models.EmailField(
        max_length=254,
        unique=True, error_messages={'unique': '이미 가입된 이메일입니다.'}
    )
    nickname = models.CharField(
        unique=True,
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

    user = models.OneToOneField(
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

    def __str__(self):
        return str(self.user_id)


# 유저 생성 시 프로필 자동생성


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_profile, sender=settings.AUTH_USER_MODEL)
