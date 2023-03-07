from django.shortcuts import render,redirect
from django.contrib import messages

from .models import Contact
# Create your views here.
def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def webDevelopment(request):
    return render(request,'web-development.html')
def mobileDevelopment(request):
    return render(request,'mobile-development.html')
def digitalMarketing(request):
    return render(request,'digital-marketing.html')
def usStaffing(request):
    return render(request,'us-staffing.html')
def domesticStaffing(request):
    return render(request,'domestic-staffing.html')
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phoneNumber=request.POST['phone']
        message=request.POST['msg']

        contact=Contact.objects.create(name=name,email=email,phoneNumber=phoneNumber,message=message)
        contact.save()
        messages.info(request,'Data Submitted Successfully')
        return redirect('contact')



        
    else:
        return render(request,'contact.html')
def careers(request):
    return render(request,'careers.html')

# Errors 
def error_404(request,exception):
    return render(request,'404.html')