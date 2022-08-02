from django import forms
from .models import User, Profile


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname']

    def signup(self, request, user):
        user.email = self.cleaned_data['email']
        user.nickname = self.cleaned_data['nickname']
        user.save()
        return user


class ProfileEditForm(forms.Form):
    nickname = forms.CharField
