from distutils.command.upload import upload
from pickle import NONE
from pyexpat import model
from tabnanny import verbose
from turtle import update
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator

class UserManager(BaseUserManager):

    def create_user(self, email, username, nickname, password=None, **extra_fields):
        """주어진 이메일, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성"""

        if not email:
            raise ValueError('이메일을 입력해 주세요')
        
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)

        user = self.model(
            email=email, 
            username=username, 
            nickname=nickname, 
            **extra_fields
            )

        user.set_password(password)

        user.save(using=self._db)

        return user


    def create_superuser(self, email, username, nickname, password, **extra_fields):
        """
        주어진 이메일, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        단, 최상위 사용자이므로 권한을 부여한다. 
        """
        user = self.create_user(
            email=email,
            username=username,
            nickname=nickname,
            password=password,
            **extra_fields
        )
        extra_fields.setdefault('is_staff', True)

        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """
    email = models.EmailField(
        max_length=254,
        unique=True
    )

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        max_length=10,
        help_text=(
            "필수기입. 10자 이하. 문자, 숫자, @/./+/-/_ 만 가능."
        ),
        validators=[username_validator],
    )

    nickname = models.CharField(
        max_length=15,
        help_text=(
            "필수기입. 15자 이하. 문자, 숫자, @/./+/-/_ 만 가능."
        ),
        validators=[username_validator],

    )

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
    is_superuser = models.BooleanField(
        default=False,
        help_text=(
        "사용자의 관리자 사이트의 제한 없는 접근 가능 여부."
        ),
    )
    is_staff = models.BooleanField(
        default=False,
        help_text=(
        "사용자의 관리자 사이트 로그인 가능 여부."
        ),
    )
    is_active = models.BooleanField(
        default=True,
        help_text=(
            "활성화 여부"
            "계정삭제 대신 비활성화"
        ),
    )

    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email" #사용자 식별자
    REQUIRED_FIELDS = ["username", "nickname"] #필수 입력값

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "user"

    def __str__(self):
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All superusers are staff
        return self.is_superuser


