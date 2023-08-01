from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from random import * 
from sendEmail.views import *


# Create your views here.
def index(request):
    return render(request, "main/index.html")

def signup(request):
    return render(request, "main/signup.html")

def join(request):
    print("테스트", request)

    name = request.POST['signupName']
    email = request.POST['signupEmail']
    pw = request.POST['signupPW']
    user = User(user_name = name, user_email = email, user_password = pw)
    user.save()

    # print("사용자 정보 저장 완료됨!! ")

    # 인증코드 하나 생성
    code = randint(1000, 9000)
    print("인증코드 생성-----------------", code) # 서버가 보낸 코드, 쿠키와 세션
    
    response = redirect("main_verifyCode") # 응답을 객체로 저장한다!
    response.set_cookie('code', code) # 인증코드
    response.set_cookie('user_id', user.id)

    print("응답 객체 완성----------------", response)

    # 이메일 발송 하는 함수 만들어보기
    # ExcelCalculate > main > views.py > join 함수 
    # 이메일 주소 2개를 준비를 해주세용
    send_result = send(email, code)
    if send_result:
        print("Main > views.py > 이메일 발송 중 완료된 거 같음....")
        return response
    else:
        return HttpResponse("이메일 발송 실패!")

def signin(request):
    return render(request, "main/signin.html")

def verifyCode(request):
    return render(request, "main/verifyCode.html")

def verify(request):
    return redirect('main_index') # 인증이 완료되면 메인 화면으로 보내줌

def result(request):
    return render(request, "main/result.html")