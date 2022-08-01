from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail

# Create your models here.
class User(AbstractUser):
  email = models.EmailField(
    max_length=254,
    unique=True
    )
  username_validator = UnicodeUsernameValidator()
  username = models.CharField(
    max_length=10,
    help_text=("필수기입. 10자 이하. 문자, 숫자, @/./+/-/_ 만 가능."),
    validators=[username_validator],
    )
  nickname = models.CharField(
    max_length=15,
    help_text=("필수기입. 15자 이하. 문자, 숫자, @/./+/-/_ 만 가능."),
    validators=[username_validator]
  )

  created_at = models.DateTimeField(auto_now_add =True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = "user"
    verbose_name_plural = "users"
  def __str__(self):
    return self.email

class Profile(models.Model):

  user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

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