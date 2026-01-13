from django.shortcuts import render,redirect,get_object_or_404
from .models import Trek,Booking
from .forms import BookingForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def register_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmed_password = request.POST.get("confirmed_password")
        
        if password != confirmed_password:
            messages.error(request,"password dont matched try again")
            return redirect("register_page")
        
        if User.objects.filter(username=username).exists():
            messages.error(request,"username already exits")
            return redirect("register_page")
        
        User.objects.create_user(username=username, password=password, email=email)
        send_mail(
            
            subject="User Registration on Django app",
            message=f"{username} has successfully registered there account on our app",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )
        return redirect("login_page")
        
    return render(request,'auth/register_page.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        User = authenticate(request, username=username,password=password)
        if User:
            login(request,User)
            return redirect("home2")
        else:
            messages.error(request,"unauthrized user!")
            
        
    return render(request,'auth/login_page.html')


def home(request):
    return render(request, 'website/index.html')


@login_required(login_url="login_page")
def home2(request):
    return render(request, 'website/index2.html')




def district_treks(request, district):
    treks = Trek.objects.filter(district=district)
    return render(request, "website/district_treks.html", {"treks": treks, "district": district})

def logout_page(request):
    logout(request)
    return redirect("home")

def trek_detail(request, trek_id):
    trek = get_object_or_404(Trek, id=trek_id)
    return render(request, "website/trek_detail.html", {"trek": trek})

def book_trek(request, trek_id):
    trek = get_object_or_404(Trek, id=trek_id)
    form = BookingForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            booking = form.save(commit=False)
            booking.trek = trek
            booking.save()
            return render(request, "website/success.html")

    return render(request, "website/book_trek.html", {"form": form, "trek": trek})




