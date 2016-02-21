from django.shortcuts import render
from django.shortcuts import redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login
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
          print("bad creds")
          return redirect('post_list')
    else:
      form = LoginForm()
    return render(request, 'login/templates/login.html', {'form':form})
      