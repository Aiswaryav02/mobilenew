from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,FormView,View
from django.contrib.auth.models import User
from .forms import  UserRegForm,LoginForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.


class Home(TemplateView):
    template_name="home.html"


class UserRegView(CreateView):
    template_name='reg.html'
    model=User
    form_class=UserRegForm
    success_url=reverse_lazy('home')
    
class LoginView(FormView):
    form_class=LoginForm
    template_name='login.html'
    def post(self,req):
            un=req.POST.get('username')
            pw=req.POST.get('password')
            user=authenticate(req,username=un,password=pw)
            if user:
                if user.usertype=="store":
                    login(req,user)
                    return redirect("shm")
                login(req,user)
                return redirect("uhm")
            else:
                messages.error(req,"incorrect password")
                return redirect("logi")



class SignOut(View):
    def get(self,req,*args,**kwargs):
        logout(req)
        return redirect('logi')


