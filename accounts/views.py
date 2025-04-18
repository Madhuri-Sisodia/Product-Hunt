from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth



def signup(request):
    if request.method == 'POST':
        print(request.POST)  # <-- Add this line to check form data

        if request.POST['password'] == request.POST['confirmPassword']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'user already exist'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Password do not matched'})
    else:
        return render(request, 'accounts/signup.html')


# def signup(request):
#     if request.method == 'POST':
       
#        if request.POST['password'] == request.POST['confirmPassword']:
#               try:
#                   user = User.objects.get( username = request.POST['username'])
#                   return render(request, 'accounts/signup.html', {'error':'user already exist'})
#               except User.DoesNotExist:
#                    user = User.objects.create_user( request.POST['username'], password= request.POST['password'])
#                    auth.login(request, user)
#                    return redirect('home')
       
#        else: 
#             return render(request, 'accounts/signup.html', {'error':'Password do not matched'})
#     else:      
#          return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['username'], password = request.POST['password'])
        if user is not None:
         auth.login(request,user)
         return redirect('home')
        else:
         return render(request, 'accounts/login.html',{'error':'username and password is invalid'})
    else:
      return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
 