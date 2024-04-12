from django.shortcuts import render,HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm,CustomAuthenticationForm

def home(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request,'signup.html',{'form':form})
def home1(request):       
          if request.method == 'POST':
                form = CustomAuthenticationForm(request, request.POST)
                if form.is_valid():
                     username = form.cleaned_data.get('username')
                     password = form.cleaned_data.get('password')
                     user = authenticate(request, username=username, password=password)
                     if user is not None:
                          login(request, user)
                          return redirect('index')
          else:
               form = CustomAuthenticationForm() 
          return render(request,'login.html',{'form':form})

def index(request):
    return render(request,'pollswebsite/pollswebsite.html')
# Create your views here.


