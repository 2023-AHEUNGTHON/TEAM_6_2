from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate

from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.db import IntegrityError
# Create your views here.

"""
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user:
            request.session['user'] = user.id
            print("login success")
            return redirect('main')
        else:
            print("login fail")
            return render(request, 'universe/login.html', {'error': '아이디나 비밀번호가 틀렸습니다.'})
    else:
        print("login fail")
        return render(request, 'universe/login.html')
    
def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('main')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        grade = request.POST['grade']
        school = request.POST['school']
        email = request.POST['email']
        major = request.POST['major']
        project = request.POST['project']
        student_id = request.POST['student_id']
        password = request.POST['password']
        available = request.POST['available']
        user = User.objects.create_user(username=username, 
                                        grade=grade, 
                                        school=school, 
                                        email=email, 
                                        major=major, 
                                        project=project, 
                                        student_id=student_id, 
                                        password=password, 
                                        available=available)
        user.save()
        print("register success")
        return redirect('login')
    else:
        print("register fail")
        return render(request, 'universe/register.html')
    
def main(request):
    categories = ['Video', 'Design', 'Photo', 'Web', 'Composing', 'Product Manager', 'IOS', 'Lyric', 'Vocal', 'Android', 'Marketing', 'Dance', 'Server', 'Advertisement', 'etc']
    return render(request, 'universe/main.html', {'categories': categories})

def board(request, category=None):
    if category:
        write = Write.objects.filter(category=category)
    else:
        write = Write.objects.all()
    return render(request, 'universe/board.html', {'write': write, 'category': category})

def post(request, category=None):
    if request.method == 'POST':
        content = request.POST['content']
        category = request.POST['category']
        user = request.user 
        write = Write(content=content, category=category, user=user)
        write.save()
        return redirect('board', category=category)
    return render(request, 'universe/post.html', {'category': category})

def comment_page(request):
    write = Write.objects.all()
    return render(request, 'universe/comment_page.html',{'write':write,})

"""
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


class Register(APIView):
    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.create( username=request.data['username'],
                                       grade=request.data['grade'],
                                       school=request.data['school'],
                                       email=request.data['email'],
                                       major=request.data['major'],
                                       project=request.data['project'],
                                       student_id=request.data['student_id'],
                                       password=request.data['password'],
                                       available=request.data['available'],)
            user.set_password(request.data['password'])
            user.save()
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except IntegrityError as e:
            return Response({"ERROR": str(e)})
        
class Login(APIView):
    def post(self, request, *args, **kwargs):
        user = authenticate(email=request.data['email'], password=request.data['password'])
        if user is None:
            return Response({'result': 'login fail'})
        else:
            token = TokenObtainPairSerializer.get_token(user)
            return Response({
                'refresh_token': str(token),
                'access_token': str(token.access_token),
                'user_id': user.id,
            })

class SearchUser(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        username = data.get('username')
        grade = data.get('grade')
        school = data.get('school')
        email = data.get('email')
        major = data.get('major')
        project = data.get('project')
        available = data.get('available')

        if username:
            user = User.objects.filter(username=username)
        elif grade:
            user = User.objects.filter(grade=grade)
        elif school:
            user = User.objects.filter(school=school)
        elif email:
            user = User.objects.filter(email=email)
        elif major:
            user = User.objects.filter(major=major)
        elif project:
            user = User.objects.filter(project=project)
        elif available:
            user = User.objects.filter(available=available)
        else:
            user = User.objects.all()

        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    
class CreatePostView(APIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.get(id = request.data['id'])
        try:
            post = Post.objects.create(title=request.data['title'],
                                       content=request.data['content'],
                                       category=request.data['category'],
                                       user=user)
            post.save()
            serializer = PostSerializer(post)
            return Response(serializer.data)
        except IntegrityError as e:
            return Response({"ERROR": str(e)})

class ReadPostView(APIView):
    def get(self, request, *args, **kwargs):
        data = request.data
        title = data.get('title')
        content = data.get('content')
        category = data.get('category')
        user = data.get('user')
        
        if title:
            post = Post.objects.filter(title=title)
        elif content:
            post = Post.objects.filter(content=content)
        elif category:
            post = Post.objects.filter(category=category)
        elif user:
            post = Post.objects.filter(user=User.objects.get(id = user))
        else:
            post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

class UpdatePostView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        id = data.get('id')

        post = Post.objects.get(id=id)
        title = data.get('title')
        content = data.get('content')
        category = data.get('category')
        
        if title:
            post.title = title
        elif content:
            post.content = content
        elif category:
            post.category = category

        post.save()
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
class DeletePostView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        id = data.get('id')
        post = Post.objects.get(id=id)
        post.delete()
        return Response({'result': 'delete success'})

class PostDetailView(APIView):
    def get(self, request, id, *args, **kwargs):
        post = Post.objects.filter(id=id).first()
        comments = Comment.objects.filter(post=post)
        user = User.objects.filter(id=post.user.id).first()
        serializer = PostCommentSerializer({"user": user, "post" : post, "comment" : comments})
        return Response(serializer.data)
    
class MatchingUserView(APIView):
    def get(self, request, *args, **kwargs):
        data = request.data
        project = data.get('project')
        major = data.get('major')

        users = User.objects.filter(project=project, major=major)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
class DetailUserView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        id = data.get('id')

        user = User.objects.filter(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
class UserProfileView(APIView):
    def get(self, request, *args, **kwargs):
        data = request.data
        id = data.get('id')

        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
class UpdateUserProfileView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        major = data.get('major')
        project = data.get('project')
        available = data.get('available')
        id = data.get('id')
        user = User.objects.get(id=id)
        user.major = major
        user.project = project
        user.available = available
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
class CreateCommentView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        content = data.get('content')
        post = Post.objects.get(id = data.get('post_id'))
        user = User.objects.get(id = data.get('user_id'))

        comment = Comment.objects.create(content=content, post=post, user=user)
        comment.save()
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
class UpdateCommentView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        comment = Comment.objects.get(id = data.get('id'))
        content = data.get('content')

        comment.content = content
        comment.save()
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
class DeleteCommentView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        comment = Comment.objects.get(id = data.get('id'))
        comment.delete()
        return Response({'result': 'delete success'})