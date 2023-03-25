from django.shortcuts import render
from home.models import Reg
from home.forms import ContactInput
# Create your views here.

def home_index(request):
    if request.method == "POST":
        contact_input = ContactInput(request.POST)
        name = request.POST['name'] 
        email = request.POST['email']
        password = request.POST['password']
        contact = request.POST['contact']
        add = Reg(name=name, email=email, password=password, contact=contact)
        add.save()
        reg = Reg.objects.all()
        return render(request, 'home/home.html', {"register": reg, "form": contact_input})
    else:
        reg = Reg.objects.all()
        contact_input = ContactInput()
        return render(request, 'home/home.html', {"register": reg, "form": contact_input})


def home_another(request):
    return render(request, 'home/another.html')