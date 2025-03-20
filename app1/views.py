from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from app1.models import RegTable,RegTable2,RegTable3
# Create your views here.

def home(request):
    return render(request,'index.html')
def training(request):
     return render(request,'training.html')
def services(request):
    return render(request,'services.html')
def form(request):
    return render(request,'form.html')
def shop(request):
    return render(request,'shop.html')
def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')
def dashboard(request):
    data=RegTable.objects.all()
    con={'Reg':data}
    return render(request,'dashboard.html',con)
def homedash(request):
    return render(request,'homedash.html')
def membership(request):
    data=RegTable2.objects.all()
    con={'Reg':data}
    return render(request,'membership.html',con)
def personaldash(request):
    data=RegTable3.objects.all()
    con={'Reg':data}
    return render(request,'personaldash.html',con)
def memform(request):
    return render(request,'memform.html')
def workout(request):
    return render(request,'workout.html')
def diet(request):
    return render(request,'diet.html')


def formabc(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        DOB=request.POST['DOB']
        gen=request.POST['gen']
        Age=request.POST['Age']
        Email=request.POST['Email']
        Pass=request.POST['Pass']
        mytext=request.POST['mytext']
        my_model=RegTable(fname=fname,lname=lname,DOB=DOB,gen=gen,Age=Age,Email=Email,Pass=Pass,mytext=mytext)
        my_model.save()
    return render(request,'submit.html')

def formmem(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        DOB=request.POST['DOB']
        gen=request.POST['gen']
        Age=request.POST['Age']
        Email=request.POST['Email']
        Pass=request.POST['Pass']
        mytext=request.POST['mytext']
        my_model=RegTable2(fname=fname,lname=lname,DOB=DOB,gen=gen,Age=Age,Email=Email,Pass=Pass,mytext=mytext)
        my_model.save()
    return render(request,'submit.html')

def trainingform(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        DOB=request.POST['DOB']
        gen=request.POST['gen']
        Payment_Method=request.POST['Payment_Method']
        PayMethod=request.POST['PayMethod']
        my_model=RegTable3(fname=fname,lname=lname,DOB=DOB,gen=gen,Payment_Method=Payment_Method,PayMethod=PayMethod)
        my_model.save()
    return render(request,'submit.html')

     
