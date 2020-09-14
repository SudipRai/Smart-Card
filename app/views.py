from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.authenticate import Authenticate,AuthenticateA
from app.models import User,Order,UserLogin,Profile
from app.forms.orderform import OrderForm
from app.forms.userform import UserForm
from app.forms.profileform import ProfileForm
import vobject

# Create your views here.

def _vcard_string(profile):
    v = vobject.vCard()
    v.add('n')
    v.n.value = vobject.vcard.Name(family=profile.fullname, given=profile.fullname)
    v.add('fn')
    v.fn.value = "%s %s" % (profile.fullname, profile.fullname)
    v.add('email')
    v.email.value = profile.email
    v.add('tel')
    v.tel.value = profile.contact
    v.tel.type_param = 'WORK'
    v.add('url')
    v.url.value = profile.website
    output = v.serialize()
    return output

def vcard(request,id):
    profile = Profile.objects.get(id=id)
    output = _vcard_string(profile)
    filename = "%s%s.vcf" % (profile.fullname, profile.fullname)
    response = HttpResponse(output, content_type="text/x-vCard")
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response

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