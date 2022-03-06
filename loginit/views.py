from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse 
from . models import saver
# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("pass")
        print(password,username)
        user = saver(username=username,password=password)
        user.save()
        return HttpResponse("Done")
    return render(request,'djangoPlayGround/index.html')
