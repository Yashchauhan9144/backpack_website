from django.shortcuts import HttpResponse
from django.shortcuts import render
from webs.models import *
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')  

def shop(request):
    data=shopproduct.objects.all()
    return render(request,'shop.html',{'value':data})

def contact(request):
    return render(request,'contact.html')

def blog(request):
    return render(request,'blog.html')

def account(request):
    return render(request,'myaccount.html')

def register(request):
    return render(request,'signup.html')

def cart(request):
    obj=cartitem.objects.all()
    return render(request,'cart.html',{'shop':obj})

def information(request):
    return render(request,'info.html')    

def store(request):
    fn = request.GET.get('nm')
    ln = request.GET.get('lnm')
    em = request.GET.get('mail')
    ta = request.GET.get('value')

    # return HttpResponse(fn,ln,em,ta)
    obj=contactinfo(fname=fn,lname=ln,email=em,tarea=ta)
    obj.save()
    return render(request,'contact.html')


def data(request):
    name=request.POST['uname']
    mailid=request.POST['mail']
    password=request.POST['pwd']
    phone=request.POST['phone']
    address=request.POST['addres']

    obj = signupinfo(uname=name,umail=mailid,pswd=password,phn=phone,adrs=address)
    obj.save()
    return render(request,'myaccount.html')

def linfo(request):
    loname=request.POST['eminm']
    lopwd=request.POST['lgpass']

    loname=st/r(loname)

    if loname is '':
        messages.warning(request, "name should not empty .. ") 
        return render(request,'myaccount.html')


    obj = signupinfo.objects.all()
    obj1 = signupinfo.objects.all().filter(uname=loname)

    for i in obj:
        if (i.uname==loname or i.umail==loname) and i.pswd==lopwd:
            # return render(request,'myaccount.html',{'data':obj1})
            messages.success(request, "Login successfull .........")
            return render(request,'myaccount.html')


    messages.error(request, "Sorry User not found in Database ....")
    return render(request,'myaccount.html')
        
def cartinfo(request):
    pid=request.POST['nm']
    pname=request.POST['nm1']
    pprice=request.POST['nm2']
    pimage=request.POST['nm3']

    # obj=shopproduct.objects.all().filter(id=pid)
    cobj=cartitem(pname=pname,price=pprice,pimage=pimage)
    cobj.save()

    obj=cartitem.objects.all()

    return render(request,'cart.html',{'shop':obj})



def delete(request):
    value=request.GET['value']
    obj=cartitem.objects.all().filter(id=value)
    obj.delete()

    output=cartitem.objects.all()
    return render(request,'cart.html',{'shop':output})

def update(request):
    value=request.GET['pid']
    pqty=request.GET['qty']
    pqty=int(pqty)
    pqty=pqty+1
    data=cartitem.objects.get(id=value)
    data.pquantity=pqty
    data.ptotalprice=int(data.ptotalprice)+50
    data.save()

    obj = cartitem.objects.all()
    return render(request,'cart.html',{'shop':obj})

def uptodate(request):
    value=request.GET['pid']
    pqty=request.GET['qty']
    # pqty=int(pqty)
    # pqty=pqty-1
    data=cartitem.objects.get(id=value)
    data.pquantity=int(data.pquantity)-1
    data.ptotalprice=int(data.ptotalprice)-50
    data.save()

    obj = cartitem.objects.all()
    return render(request,'cart.html',{'shop':obj})      