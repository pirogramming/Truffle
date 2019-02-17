from django.urls import path
from . import views

app_name = 'playlists'

urlpatterns = [
    # path('',views.playlist_list,name='playlist_list'),
    path('upload',views.upload,name='upload'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('search', views.search_view, name='search'),
    path('my_list',views.my_list,name='my_list'),
    path('edit_mine/<int:id>',views.edit_mine,name='edit_mine'),
    path('commment/<int:id>',views.comment,name='comment'),
    path('user_list/<int:id>', views.user_list, name='user_list'),
]

