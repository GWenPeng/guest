from django.shortcuts import render
from django.http import  HttpResponse,HttpResponsePermanentRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
   # return HttpResponse('Hello Django!')
     return render(request,"index.html")
def login_action(request):
     if request.method=='POST':
         username=request.POST.get("username","")
         password=request.POST.get("password","")
         user=auth.authenticate(username=username,password=password)#authenticate函数接受username 和password ,并且在用户名和密码正确的情况下返回一个user对象，否则返回None
         if user is not None:
             auth.login(request,user)#登陆
        # if username=='admin'and password=='admin123':
             #return  HttpResponse("Login Success!")登陆成功返回的内容
             # return render(request,"event_manage.html")#返回event_manage.hmtl模板
             reponse=HttpResponsePermanentRedirect('/event_manage/')#对路径重定向，从而使登陆成功的请求指向event_manage/目录,即：http://127.0.0.1:8000/event_manage/
             #reponse.set_cookie('user',username,3600) #添加浏览器cookie

             request.session['user']=username

             return  reponse
         else:
             return  render(request,"index.html",{'error':'username or password error!'})
@login_required
def event_manage(request):
     #username=request.COOKIES.get('user','')#获取浏览器cookie
     username=request.session.get('user','')
     return render(request,'event_manage.html',{'user':username})
