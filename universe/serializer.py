from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostCommentSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True)
    comment = CommentSerializer(read_only=True, many=True)
    class Meta:
        model = Post
        fields = ['post', 'comment']

