from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here
def index(request):
#    return HttpResponse("Hello Django!")
    return render(request,"index.html")
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if username == 'admin' and password == 'admin123':
#            return HttpResponse('login success!')
            return HttpResponseRedirect('/event_manage/')
        else:
            return render(request,'index.html',{'error':'username or password error!'})
def event_manage(request):
    return render(request,"event_manage.html")



