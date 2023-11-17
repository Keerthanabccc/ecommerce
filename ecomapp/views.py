from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    return render(request,'index.html')






def reg(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        username=request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        detaddress=request.POST.get('detaddress')
        fiimg=request.FILES.get('fiimg')

        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password==cpassword:
            a=register(fname=fname,lname=lname,username=username,email=email,phone=phone,gender=gender,dob=dob,address=address,detaddress=detaddress,password=password,fiimg=fiimg)
            a.save()
            return HttpResponse("Registration Successfull")
        else:
            return HttpResponse("Registration Incomplete")
    return render(request,'register.html')




def log(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        a=register.objects.all()
        for i in a:
            if(i.email==email and i.password==password):
                request.session['id']=i.id
                return redirect(display)
        else:
            return HttpResponse("login failed")
    return render(request,'login.html')



def up(request):
    if request.method=='POST':
        pname=request.POST.get('pname')
        fileimage=request.FILES.get('fileimage')
        pdes=request.POST.get('pdes')
        price=request.POST.get('price')
        b=upload(pname=pname,fileimage=fileimage,pdes=pdes,price=price)
        b.save()
        return HttpResponse('Fileupload Success')
    return render(request,'upload.html')




def display(request):
    id=request.session['id']
    a=register.objects.get(id=id)
    fiimg=str(a.fiimg).split('/')[-1]
    return render(request,'display.html',{'data':a,'fiimg':fiimg})



def update_data(request,id):
    a=register.objects.get(id=id)
    img = str(a.fiimg).split('/')[-1]
    if request.method=='POST':
        a.fname = request.POST.get('fname')
        a.lname = request.POST.get('lname')
        a.email = request.POST.get('email')
        a.phone = request.POST.get('phone')
        if str(request.POST.get('gender')) == 'female' or str(request.POST.get('gender')) == 'male' or str(request.POST.get('gender'))=='other':
            a.gender = request.POST.get('gender')

        if len(str(request.POST.get('dob')))>0:
            a.dob=request.POST.get('dob')
        else:
            a.save()
        a.fiimg = request.FILES['fiimg']
        a.address = request.POST.get('address')
        a.detaddress = request.POST.get('detaddress')
        a.save()
        return redirect(display)
    return render(request,'editpro.html',{'data':a,'fiimg':img})



def car(request):
    return render(request,'card.html')



def men(request):
    a=model.objects.all()
    return render(request,'mencollection.html',{'a':a})

