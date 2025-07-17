from django.shortcuts import render
from django.http import HttpResponse
from webapp.models import signin
# Create your views here.

def index(request):
    return render(
   request, 'index.html')
def Signin(request):
    data = signin.objects.all()
    
    if request.method=="POST":
        Uname = request.POST.get('Username','')
        Pass = request.POST.get('Password','')
        print('Reach')

        FavCity = request.POST.get('FaviouriteCity','')

        data = signin(Username= Uname,Password=Pass,FaviouriteCity=FavCity)
        data.save()
        return HttpResponse("<h1 style='color:red;'>Data Inserted Succesfully</h1>")
    

    return render(
        request, 'signin.html',{"messages":data}
    )
    
def Service(request):
    return render(
        request, 'services.html'
    )