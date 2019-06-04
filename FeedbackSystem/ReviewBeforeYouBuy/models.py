from django.db import models

# Create your models here.

class Admin(models.Model):
	admin_name = models.CharField(max_length=100)

class Mobile(models.Model):
	m_id = models.AutoField(primary_key="true")
	m_name = models.CharField(max_length=50)
	m_price = models.CharField(max_length=50)
	m_photo_link = models.CharField(max_length=300)
	m_content_link = models.CharField(max_length=300)

class Laptop(models.Model):
	l_id = models.AutoField(primary_key="true")
	l_name = models.CharField(max_length=50)
	l_price = models.CharField(max_length=50)
	l_photo_link = models.CharField(max_length=300)
	l_content_link = models.CharField(max_length=300)

class Cameras(models.Model):
	c_id = models.AutoField(primary_key="true")
	c_name = models.CharField(max_length=50)
	c_price = models.CharField(max_length=50)
	c_photo_link = models.CharField(max_length=300)
	c_content_link = models.CharField(max_length=300)

class Smart_Watches(models.Model):
	s_id = models.AutoField(primary_key="true")
	s_name = models.CharField(max_length=50)
	s_price = models.CharField(max_length=50)
	s_photo_link = models.CharField(max_length=300)
	s_content_link = models.CharField(max_length=300)

class Electronic_Accessory(models.Model):
	e_id = models.AutoField(primary_key="true")
	e_name = models.CharField(max_length=50)
	e_price = models.CharField(max_length=50)
	e_photo_link = models.CharField(max_length=300)
	e_content_link = models.CharField(max_length=300)

class Computer_Hardware(models.Model):
	h_id = models.AutoField(primary_key="true")
	h_name = models.CharField(max_length=50)
	h_price = models.CharField(max_length=50)
	h_photo_link = models.CharField(max_length=300)
	h_content_link = models.CharField(max_length=300)

class Users(models.Model):
	u_id = models.AutoField(primary_key="true")
	fname = models.CharField(max_length=50)
	lname = models.CharField(max_length=50)
	uname = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	mnumber = models.CharField(max_length=50)

class Mobile_Feedback(models.Model):
	m_feedback_id=models.AutoField(primary_key="true")
	m_feedback=models.CharField(max_length=100)

class Laptop_Feedback(models.Model):
	l_feedback_id=models.AutoField(primary_key="true")
	l_feedback=models.CharField(max_length=100)

class Cameras_Feedback(models.Model):
	c_feedback_id=models.AutoField(primary_key="true")
	c_feedback=models.CharField(max_length=100)

class Smart_Watches_Feedback(models.Model):
	s_feedback_id=models.AutoField(primary_key="true")
	s_feedback=models.CharField(max_length=100)

class Electronic_Accessory_Feedback(models.Model):
	e_feedback_id=models.AutoField(primary_key="true")
	e_feedback=models.CharField(max_length=100)

class Computer_Hardware_Feedback(models.Model):
	c_feedback_id=models.AutoField(primary_key="true")
	c_feedback=models.CharField(max_length=100)	

class Notify(models.Model):
	notify_email = models.CharField(max_length=30,primary_key="true")