from django.shortcuts import render,redirect
from . models import Userlog

# Create your views here.
def home(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        comments = request.POST['comments']
        Userlog.objects.create(name=name, email=email, comments=comments)
        return redirect('feedbackpart.home')
    else:
        return render(request,'feedbackpart/1.html')
