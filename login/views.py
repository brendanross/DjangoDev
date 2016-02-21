from django.shortcuts import render
from django.shortcuts import redirect
from .forms import LoginForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def login_user(request):
    if request.method == "POST":
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(username=username, password=password)
      if user is not None:
          if user.is_active:
              login(request, user)
              return redirect('post_list')
          else:
              print("not active")
              return redirect('post_list')
      else:
          #should redirect to /login/ with message
          print("bad creds")
          return redirect('post_list')
    else:
      form = LoginForm()
    return render(request, 'login/templates/login.html', {'form':form})

def logout_user(request):
  logout(request)
  return redirect('post_list')

def register_user(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    user = User.objects.create_user(username, email, password)
    return redirect('post_list')
  else:
    form = UserForm()
  return render(request, 'login/templates/register.html', {'form':form})