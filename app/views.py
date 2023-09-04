from django.shortcuts import render,redirect
from .models import Products,cat,cartItem
from .forms import LoginForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import auth
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def home(request):
    products = Products.objects.all()
    cart = cartItem.objects.all()

 
    return render(request,"home.html",{'categories':cat,'products':products})
def products(request,name):
    products = Products.objects.filter(category = name)

    

    return render(request,"products.html",{"products":products,"name":name,'categories':cat})

def Login_user(request):
    form = LoginForm
    if request.method == "POST":
        form = LoginForm(request,data = request.POST)

        if form.is_valid():
            print("helllo")
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username = username, password = password)
            if user is not None:
                auth.login(request, user)
                return redirect("/")
    return render(request,"loginform.html",{'form':form})

def logout_user(request):
    auth.logout(request)
    return redirect("/")
def product_detail(request,id):
    product = Products.objects.get(pk = id)
    return render(request,"product_detail.html",{"product":product})
@login_required(login_url = 'login')
def add_cart(request,id):
    items = cartItem
    d = Products.objects.get(pk=id)
    cartitemm = items.objects.filter(item=d,user= request.user).exists()
    print(cartitemm)
    if cartitemm:
        print("exists")
        i = items.objects.get(item = d.id)
        i.quantity+=1
        i.save()
        return HttpResponse("quantity added by 1")

    else:
        items.objects.create(item = d,user=request.user)   
        return HttpResponse("added to the cart")
def cart(request):
    cartitems = cartItem.objects.all().filter(user=request.user)

    
    return render(request,"cart.html",{"cartitem":cartitems})
