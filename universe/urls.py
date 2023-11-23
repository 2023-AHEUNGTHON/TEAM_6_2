
from django.urls import path
from .views import board, comment_page, main, post

urlpatterns = [
    path('', main, name='main'),
    path('board/<str:category>/', board, name='board'),
    path('post/<str:category>/',post, name='post'),
    path('comment_page/',comment_page,name='comment_page'),
    
]