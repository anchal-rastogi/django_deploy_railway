from django.shortcuts import render, redirect
from.models import*

# Create your views here.

def index(request):
    return render(request,"index.html")

def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def education(request):
    return render(request,"education.html")

def experties(request):
    return render(request,"experties.html")

def project(request):
    return render(request,"project.html")

def contact(request):
    if request.method=="post":
        Name=request.POST.get("name")
        Email=request.POST.get("email")
        Mobile=request.POST.get("mob")
        Message=request.POST.get("msg")
        tblcontact(name=Name,email=Email,mobile=Mobile,message=Message).save()
        return redirect("<script> alert('Data stored Successfully');location.href='/contact/'</script>")
    return render(request,"contact.html")


