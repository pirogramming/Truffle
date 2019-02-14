from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import re
from django.forms import ValidationError
from django.utils.translation import gettext, gettext_lazy as _


def phone_number_check(number):
    pass
    # if not re.match(r'^010-[1-9]\d{3}-\d{4}$', number):
    #     raise ValidationError('{}는 형식이 틀렸습니다.\n010-xxxx-xxxx 형식으로 입력하세요.'.format(number)

class ProfileForm(forms.ModelForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '닉네임'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '이메일'}))
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '이름'}))
    pw1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '비밀번호'}))
    pw2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '비밀번호 재입력'}))

    def clean(self):
        pw1 = self.cleaned_data['pw1']
        pw2 = self.cleaned_data['pw2']

        if pw1 == pw2:
            self.cleaned_data['pw'] = pw1
        else:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')

    class Meta:
        model = Profile
        fields = ('address','phone_number')
        widgets = {
            'phone_number':forms.TextInput(attrs={'class':'form-control','placeholder':'전화번호'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'주소'}),
        }


class LoginForm(forms.Form):
    email = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '이메일'}))
    pw = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '비밀번호'}))
    
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
    userid = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '아이디를 입력하세요.'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': '등록한 이메일을 입력하세요.'}))

class SoSignupForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '닉네임을 입력하세요.'}))
    pw1 = forms.EmailField(label='', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': '비밀번호를 입력하세요.'}))
    pw2 = forms.EmailField(label='', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': '비밀번호를 확인해주세요.'}))
