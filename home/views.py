from django.shortcuts import render,HttpResponse
from home.models import Contact


# Create your views here.
def home(request):
    #return HttpResponse("This is my homepage ")
    context= {"name":"Harry","course":"Django"}
    return render(request,'home.html',context)
    



def info(request):
    #return HttpResponse("This is my about ")
    return render(request,'info.html')

def projects(request):
    #eturn HttpResponse("This is my projects ")
    return render(request,'projects.html')

def contact(request):
    if request.method=="POST":
        #print("This is post ")
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        #print(name,email,phone,desc)
        ins=Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("the data has been written to db")



    #return HttpResponse("This is my contact ")
    return render(request,'contact.html')
