from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate

from .models import *

# Create your views here.
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

def comment_page(request, post_number):
    post = Write.objects.get(post_number=int(post_number))
    comments = post.comments.all()
    print(comments)
    return render(request, 'universe/comment_page.html', {'post': post, 'comments': comments})

def add_comment(request, post_number):
    if request.method == 'POST':
        post = Write.objects.get(post_number=post_number)
        user = request.user
        text = request.POST['comment_text']
        Comment.objects.create(user=user, text=text, write=post)
        
    return redirect('comment_page', post_number=post_number)
