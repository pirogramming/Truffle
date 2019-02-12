from django.urls import path
from django.shortcuts import redirect
from . import views
from allauth.account.views import SignupView, LogoutView

urlpatterns = [
    path('', views.profile_view, name='profile'),
    path('signup', views.signup, name='signup'),
    path('login', views.login_view, name='login'),
    path('slogin', views.slogin, name='slogin'),
    path('logout', views.logout_view, name='logout'),
    path('edit', views.edit, name='edit'),
    path('edit_pw', views.edit_pw, name='edit_pw'),
    path('changepw', views.changepw, name='changepw'),
    path('check', views.check, name='check'),    #  todo 소셜로그인 후 특정 주소로 리다이렉트하고 프로필 생성하기. 
    path('social/signup/', views.connect, name='connect')
]
