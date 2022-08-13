from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content']
        labels = {'title': '한줄평', 'content': '리뷰'}

    def save(self, **kwargs):
        review = super().save(commit=False)         # 부몽메서드 호출
        review.user = kwargs.get('user', None)
        review.book = kwargs.get('book', None)
        review.save()
        return review
