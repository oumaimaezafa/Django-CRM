from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def hell_world(request):
     #ceck to see if loggin in 
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            #autheticate
            user=authenticate(request,username=username,password=password)
            if user is not None:
                 login(request,user)
                 messages.success(request,"You have Been Logeed In  !!")
                 return redirect('home')
            else :
                 messages.success(request,"There was an error ,Please Try Again .... ")
                 return redirect('home') 

    
             
             
        return render(request,'home.html',{})


def logout_user(request):
    logout(request)
    messages.success(request,"You have been Logged Out ......")
    return redirect('home')

def register_user(request):
     return render(request,'register.html',{})


