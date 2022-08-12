from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content']
        labels = {'title': '한줄평',
                  'content': '리뷰'}
