from django.shortcuts import render

# Create your views here.
# hello/views.py

def home(request): #view는 기능이기 때문에 함수로 구현
  #기본 홈페이지 만 띄우기여서 return만 해줌
    return render(request, 'home.html')