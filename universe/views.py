from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from universe.models import Write

# Create your views here.
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
        write = Write(content=content, category=category)
        write.save()
        return redirect('board', category=category)
    return render(request, 'universe/post.html', {'category': category})

def comment_page(request):
    write = Write.objects.all()
    return render(request, 'universe/comment_page.html',{'write':write,})

