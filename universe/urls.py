from django.urls import path, include
from .views import *
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('User', UserViewSet, basename='User')
routers.register('Post', PostViewSet, basename='Post')
routers.register('Comment', CommentViewSet, basename='Comment')

urlpatterns = [
    path('', include(routers.urls)),
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('search/', SearchUser.as_view(), name='search'),
    path('post/<int:id>/', PostDetailView.as_view(), name='post_detail'),
    path('readpost/', ReadPostView.as_view(), name='readpost'),
    path('createpost/', CreatePostView.as_view(), name='createpost'),
    path('updatepost/', UpdatePostView.as_view(), name='updatepost'),
    path('deletepost/', DeletePostView.as_view(), name='deletepost'),
    path('createcomment/', CreateCommentView.as_view(), name='createcomment'),
    path('updatecomment/', UpdateCommentView.as_view(), name='updatecomment'),
    path('deletecomment/', DeleteCommentView.as_view(), name='deletecomment'),
    path('matching/', MatchingUserView.as_view(), name='Matching'),
    path('userprofile/', UserProfileView.as_view(), name='userprofile'),
    path('updateuserprofile/', UpdateUserProfileView.as_view(), name='updateprofile'),
]