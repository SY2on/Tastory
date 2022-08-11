from django import forms
from .models import User, Profile


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname']
        labels = {'nickname': '닉네임'}

    def signup(self, request, user):
        user.email = self.cleaned_data['email']
        user.nickname = self.cleaned_data['nickname']
        user.save()
        return user


class ProfileEditForm(forms.ModelForm):
    nickname = forms.CharField(max_length=15, label='닉네임')

    class Meta:
        model = Profile
        fields = ['introduction', 'profile_img']
