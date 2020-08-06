from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.authenticate import Authenticate,AuthenticateA
from app.models import User,Order,UserLogin,Profile
from app.forms.orderform import OrderForm
from app.forms.userform import UserForm
from app.forms.profileform import ProfileForm
# Create your views here.



def adminlogin(request):
	return render(request,'adminlogin.html')

def entry(request):
	request.session['email']=request.POST['email']
	request.session['password']=request.POST['password']
	return redirect('/dashboard')
@AuthenticateA.valid_admin
def dashboard(request):
	orders=Order.objects.all()
	return render(request,"dashboard.html",{'orders':orders})

def submit(request):
	if request.method=="POST":
		form=OrderForm(request.POST,request.FILES)
		form.save()
		return redirect('/home')

	form=OrderForm()
	return render(request,'checkout.html',{'form':form})

def checkout(request):
	return render(request,'checkout.html')

def login(request):
	return render(request,'login.html')

def adduser(request):
	if request.method=="POST":
		form=UserForm(request.POST,request.FILES)
		form.save()
		return redirect('/logindetail')


	form=UserForm()
	return render(request,"adduserlogin.html",{'form':form})

def customerlogin(request):
	users=UserLogin.objects.all()
	return render(request,"customerlogin.html",{'users':users})

def home(request):
	return render(request,"home.html")



def check(request):
	request.session['username']=request.POST['username']
	request.session['password']=request.POST['password']
	return redirect('/profile')

@Authenticate.valid_user
def profile(request):
	profile=Profile.objects.all()
	return render(request,'profile.html',{'profile':profile})


def profileview(request):
	profile=Profile.objects.all()
	return render(request,'profileshow.html',{'profile':profile})

def editform(request,id):
	edit=Profile.objects.get(id=id)
	return render(request,'editform.html',{'edit':edit})



def save(request,id):
	edit=Profile.objects.get(id=id)
	form=ProfileForm(request.POST,instance=edit)
	form.save()
	return redirect('/profile')

def profiledetail(request):
	profiles=Profile.objects.all()
	return render(request,'profiledetail.html',{'profiles':profiles})


def addprofile(request):
	if request.method=="POST":
		form=ProfileForm(request.POST,request.FILES)
		form.save()
		return redirect('/profiledetail')


	form=UserForm()
	return render(request,"addprofile.html",{'form':form})