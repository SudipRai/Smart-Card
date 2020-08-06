from django.db import models

# Create your models here.
class User(models.Model):
	id:models.AutoField(auto_created=True,primary_key=True)
	username=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=100)

	class Meta:
		db_table="user"


class Order(models.Model):
	id:models.AutoField(auto_created=True,primary_key=True)
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	address1=models.CharField(max_length=100)
	address2=models.CharField(max_length=100)
	city=models.CharField(max_length=200)
	state=models.CharField(max_length=200)
	zipcode=models.CharField(max_length=200)
	phonenumber=models.CharField(max_length=100)
	totalcost=models.IntegerField(max_length=100)
	cardname=models.CharField(max_length=100)
	cardnumber=models.CharField(max_length=100)
	cvv=models.CharField(max_length=100)
	expiration=models.CharField(max_length=100)
	class Meta:
		db_table="order"


class UserLogin(models.Model):
	id:models.AutoField(auto_created=True,primary_key=True)
	username=models.CharField(max_length=100)
	password=models.CharField(max_length=100)

	class Meta:
		db_table="userlogin"


class Profile(models.Model):
	id:models.AutoField(auto_created=True,primary_key=True)
	image=models.ImageField(default="img.jpg")
	fullname=models.CharField(max_length=100)
	address=models.CharField(max_length=100)
	companyname=models.CharField(max_length=100)
	bio=models.CharField(max_length=200)
	email=models.CharField(max_length=100)
	contact=models.CharField(max_length=100)
	website=models.CharField(max_length=100)
	instagram=models.CharField(max_length=100)
	facebook=models.CharField(max_length=100)
	twitter=models.CharField(max_length=100)
	google=models.CharField(max_length=100)
	whatsapp=models.CharField(max_length=100)
	youtube=models.CharField(max_length=100)

	class Meta:
		db_table="profile"