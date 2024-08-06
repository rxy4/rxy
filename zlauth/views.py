import random
import string

from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http.response import JsonResponse
from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_http_methods

from .forms import RegisterForm, LoginForm
from .models import CaptchaModel

User = get_user_model()


# Create your views here.
def zllogin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user = User.objects.filter(email=email).first()
            if user and user.check_password(password):
                login(request, user)

                if not remember:
                    request.session.set_expiry(0)
                return redirect('/blog/')
            else:
                print('邮箱或密码错误')
                # form.add_error('email','邮箱或密码错误')
                # return render(request,'login.html',{'form':form})
                return redirect(reverse('zlauth:login'))


def zllogout(request):
    logout(request)
    return redirect('/blog')


@require_http_methods(['GET', 'POST'])
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            try:
                # 创建用户
                User.objects.create_user(email=email, username=username, password=password)
                # 注册成功，跳转到登录页面
                return redirect(reverse('zlauth:login'))
            except Exception as e:
                # 处理用户创建时的异常（如唯一性约束失败）
                print("User creation failed:", e)
                return render(request, 'register.html', {'form': form, 'error': '用户创建失败，请重试。'})

        else:
            # 表单验证失败，返回注册页面并显示错误信息
            return render(request, 'register.html', {'form': form, 'errors': form.errors})


def send_email_captcha(request):
    email = request.GET.get('email')
    if not email:
        return JsonResponse({"code": 400, "message": "必须传递邮箱"})
    captcha = "".join(random.sample(string.digits, 4))
    CaptchaModel.objects.update_or_create(email=email, defaults={'captcha': captcha})
    send_mail("rxy博客注册验证码", message=f"您的注册验证码是:{captcha}", recipient_list=[email], from_email=None)
    return JsonResponse({"code": 200, "message": "邮箱验证码发送成功"})
