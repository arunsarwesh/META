from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/acc/login/')
        else:
            return render(request, 'registration/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})   
# Create your views here.
def lout(request):
     logout(request)
     return redirect('/')
def index(request):
        return render(request, 'registration/index.html')