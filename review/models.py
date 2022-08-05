from django.db import models

from ast import Delete
from tabnanny import verbose
from common.models import User
import os

# Create your models here.

class Book(models.Model):
    title = models.TextField()
    img_url = models.TextField()
    author = models.TextField()
    book_info = models.TextField()
    isbn = models.TextField(unique=True)
    pubdate = models.DateField()
    publisher = models.TextField()
    category = models.TextField()

    def __str__(self):
        return self.title

class Review(models.Model):

    STAT_CHOICE = (
        ('PUBLIC', 'Public'),
        ('PRIVATE', 'Private'),
        ('DELETED', 'Deleted')
    )
    review_id = models.BigAutoField(primary_key=True)

    user_id = models.ForeignKey(
        'users.User', on_delete=models.SET_NULL, db_column="user_id", null=True)

    #book_id = models.ForeignKey("Book", related_name="book", on_delete=models.CASCADE, db_column="book_id")

    title = models.CharField(
        max_length=50, help_text="Review title", blank=False, null=False)

    content = models.TextField(
        help_text="Review content", blank=False, null=False)

    status = models.CharField(
        max_length=7, help_text="Review status", choices=STAT_CHOICE, default='PUBLIC')

    created_at = models.DateTimeField(
        auto_now_add=True, help_text="Review created_at")

    updated_at = models.DateTimeField(
        auto_now=True, help_text="Review updated_at")

    class Meta:
        verbose_name = "review"
        verbose_name_plural = "reviews"
    def __str__(self):
        return self.title

class ReviewImg(models.Model):

    STAT_CHOICE = (
        ('ACTIVE', 'Active'),
        ('DELETED', 'Deleted')
    )

    review_img_id = models.BigAutoField(primary_key=True)

    review_id = models.ForeignKey(
        Review, on_delete=models.CASCADE, db_column="review_id")

    def review_img_upload_to(instance, filename):
        return os.path.join(instance.name, filename)

    img = models.ImageField(
        upload_to=review_img_upload_to,
        null=True
    )
    status = models.CharField(
        max_length=7, help_text="Review_img status", choices=STAT_CHOICE, default='ACTIVE')

    created_at = models.DateTimeField(
        auto_now_add=True, help_text="Review_img created_at")

    updated_at = models.DateTimeField(
        auto_now=True, help_text="Review_img updated_at")

    class Meta:
        verbose_name = "reveiw_img"
        verbose_name_plural = "review_imgs"


class UserReviewLike(models.Model):

    STAT_CHOICE = (
        ('ACTIVE', 'Active'),
        ('DELETED', 'Deleted')
    )

    user_review_like_id = models.BigAutoField(primary_key=True)

    user_id = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, db_column="user_id")

    review_id = models.ForeignKey(
        Review, on_delete=models.CASCADE, db_column="review_id")

    status = models.CharField(
        max_length=7, help_text="좋아요 활성화 active/deleted", choices=STAT_CHOICE, default='ACTIVE')

    class Meta:
        verbose_name = "user_review_like"
        verbose_name_plural = "user_review_likes"


class UserReviewScrap(models.Model):
    STAT_CHOICE = (
        ('ACTIVE', 'Active'),
        ('DELETED', 'Deleted')
    )

    user_review_scrap_id = models.BigAutoField(primary_key=True)

    user_id = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, db_column="user_id")

    review_id = models.ForeignKey(
        Review, on_delete=models.CASCADE, db_column="review_id")

    status = models.CharField(
        max_length=7, help_text="스크랩 활성화 active/deleted", choices=STAT_CHOICE, default='ACTIVE')

    class Meta:
        verbose_name = "user_review_scrap"
        verbose_name_plural = "user_review_scraps"


class Comment(models.Model):
    STAT_CHOICE = (
        ('ACTIVE', 'Active'),
        ('DELETED', 'Deleted')
    )
    comment_id = models.BigAutoField(primary_key=True)

    user_id = models.ForeignKey("users.User", related_name="user",
                                on_delete=models.SET_NULL, db_column="user_id", null=True)

    review_id = models.ForeignKey(
        Review, on_delete=models.CASCADE, db_column="review_id")

    content = models.CharField(max_length=200, help_text="Comment content")

    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE)

    status = models.CharField(
        max_length=7, choices=STAT_CHOICE, default='ACTIVE')

    created_at = models.DateTimeField(
        auto_now_add=True, help_text="Comment created_at")

    updated_at = models.DateTimeField(
        auto_now=True, help_text="Comment updated_at")


class UserCommentLike(models.Model):
    STAT_CHOICE = (
        ('ACTIVE', 'Active'),
        ('DELETED', 'Deleted')
    )
    user_comment_like_idx = models.BigAutoField(primary_key=True)

    user_id = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, db_column="user_id")

    comment_id = models.ForeignKey(
        Comment, on_delete=models.CASCADE, db_column="comment_id")

    status = models.CharField(
        max_length=7, choices=STAT_CHOICE, default='ACTIVE')

