
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('board/<str:category>/', board, name='board'),
    path('post/<str:category>/',post, name='post'),
    path('comment_page/',comment_page,name='comment_page'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
]