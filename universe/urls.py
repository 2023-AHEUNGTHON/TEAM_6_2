
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('board/<str:category>/', board, name='board'),
    path('post/<str:category>/',post, name='post'),
    path('comment_page/<str:post_number>',comment_page,name='comment_page'),
    path('add_comment/<int:post_number>/', add_comment, name='add_comment'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
]