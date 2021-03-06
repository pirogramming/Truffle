from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import re
from django.forms import ValidationError
from django.utils.translation import gettext, gettext_lazy as _

class ProfileForm(forms.ModelForm):
    username = forms.CharField(label='닉네임', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '닉네임'}))
    email = forms.EmailField(label='이메일', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '이메일'}))
    name = forms.CharField(label='이름', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '이름'}))
    pw1 = forms.CharField(label='비밀번호', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '비밀번호'}))
    pw2 = forms.CharField(label='비밀번호 재입력', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '비밀번호 재입력'}))
    
    
    def clean(self):
        pw1 = self.cleaned_data['pw1']
        pw2 = self.cleaned_data['pw2']

        if pw1 == pw2:
            self.cleaned_data['pw'] = pw1
        else:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')

    class Meta:
        model = Profile
        fields = ('phone_number',)
        help_texts = {'phone_number': "ex) 01X-XXX-XXXX",}
        widgets = {
            'phone_number':forms.TextInput(attrs={'class':'form-control','placeholder':'전화번호'}),
        }

class LoginForm(forms.Form):
    email = forms.EmailField(label='이메일', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '이메일'}))
    pw = forms.CharField(label='비밀번호', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '비밀번호'}))
    
class EditForm(forms.Form):
    username = forms.CharField(label='아이디', required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': '아이디'}))
    email = forms.EmailField(label='이메일',required=False, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': '이메일'}))
    photo = forms.ImageField(label='프로필 사진', required=False, widget=forms.FileInput(attrs={'class':'form-control', 'placeholder': '프로필사진'}))
# class EditForm(forms.ModelForm):
#     class Meta:
#         model=Profile
#         fields='__all__'
        
class NewpwForm(forms.Form):
    current_pw = forms.CharField(label='현재 비밀번호', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': '현재 비밀번호'}))
    new_pw1 = forms.CharField(label='새 비밀번호', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': '새 비밀번호'}))
    new_pw2 = forms.CharField(label='비밀번호 재입력', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': '비밀번호 재입력'}))

class ChangepwForm(forms.Form):
    userid = forms.CharField(label='아이디를 입력하세요.', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '아이디를 입력하세요.'}))
    email = forms.EmailField(label='등록한 이메일을 입력하세요.', widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': '등록한 이메일을 입력하세요.'}))

class CheckForm(forms.Form):
    username = forms.CharField(label='닉네임을 입력하세요.', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '닉네임을 입력하세요.'}))
    pw1 = forms.CharField(label='비밀번호를 입력하세요.', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': '비밀번호를 입력하세요.'}))
    pw2 = forms.CharField(label='비밀번호를 확인해주세요.', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': '비밀번호를 확인해주세요.'}))
