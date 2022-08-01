from django import forms
from .models import User


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'nickname']

    def signup(self, request, user):
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        user.nickname = self.cleaned_data['nickname']
        user.save()
        return user
