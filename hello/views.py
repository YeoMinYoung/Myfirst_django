from django.shortcuts import render, redirect
from .models import Blog
# Create your views here.
# hello/views.py

def home(request): #view는 기능이기 때문에 함수로 구현
  #기본 홈페이지 만 띄우기여서 return만 해줌
    blogs = Blog.objects 
    #view에서만 사용할 변수를 만들어 model의 객체를 넣어주기,
    #html에서 변수 return
    return render(request, 'home.html',{'blogs':blogs})

def new(request):
  return render(request, 'new.html')

def create(request):
  if(request.method == 'POST'):
    post = Blog()
    post.title = request.POST['title']
    post.body = request.POST['body']
    post.save()
  return redirect('home')
