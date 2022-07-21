from django.db import models

# Create your models here.
class Review(models.Model):
    
    STAT_CHOICE = (
      ('PUBLIC','Public'),
      ('PRIVATE', 'Private'),
      ('DELETED', 'Deleted')
    )
    review_id = models.BigAutoField(primary_key=True)

    user_id = models.ForeignKey("User", related_name="user", on_delete=models.SET_NULL, db_column="user_id", null=True)
    
    #book_id = models.models.ForeignKey("Book", related_name="book", on_delete=models.SET_NULL, db_column="user_id", null=True)
    
    title = models.CharField(max_length=50, help_text="Review title", blank=False, null=False)

    content = models.TextField(help_text="Review content", blank=False, null=False)

    status = models.CharField(help_text="Review status", choices=STAT_CHOICE)

    created_at = models.DateTimeField(auto_now_add =True, help_text="Review created_at")

    updated_at = models.DateTimeField(auto_now=True, help_text="Review updated_at")
