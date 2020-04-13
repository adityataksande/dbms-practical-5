from django.db import models


# Create your models here.
class event(models.Model):
    id = models.IntegerField(primary_key=True)
    eve_name = models.CharField(max_length=30)
    eve_type = models.CharField(max_length=30)
    dept_faculty_name = models.CharField(max_length=30,unique=True)
    vol_head = models.CharField(max_length=30)

class student(models.Model):
    stu_id = models.IntegerField(primary_key=True)
    stu_name = models.CharField(max_length=30)
    stu_mobileno = models.IntegerField()
    stu_email = models.EmailField(max_length=40)
    stu_address = models.CharField(max_length=30)
    stu_dept = models.CharField(max_length=30)
    semister = models.IntegerField()

class student_details(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.IntegerField(unique=True)
    daa = models.IntegerField()
    dbms = models.IntegerField()
    sepm = models.IntegerField()
    sp = models.IntegerField()
    total = models.IntegerField()
    percentage = models.IntegerField()