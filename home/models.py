import email
from math import fabs
from pickle import TRUE
from tkinter import Widget
from unicodedata import name
from django.db import models
from django import forms
Hostel_choices = (
    ('1','HOSTEL 1'),
    ('2','HOSTEL 2'),
    ('3','HOSTEL 3'),
    ('4','HOSTEL 4'),
    ('5','HOSTEL 5'),
    ('6','HOSTEL 6'),
    ('7','HOSTEL 7'),
    ('8','HOSTEL 8'),
    ('9','HOSTEL 9'),
    ('10','HOSTEL 10'),
    ('11','HOSTEL 11'),
    ('12','HOSTEL 12'),
    ('13','HOSTEL 13'),
    ('14','HOSTEL 14'),
    ('15','HOSTEL 15'),
    ('16','HOSTEL 16'),
    ('17','HOSTEL 17'),
    ('18','HOSTEL 18')
    
)
IITian_choices = (
    ('1','Yes'),
    ('2','No')
)

Sector_choices = (
    ('1','FMCG'),
    ('2','FINTECH'),
    ('3','EDTECH'),
    ('4','CONSULTING'),
    ('5','IT'),
    ('6','ECOMMERCE'),
    ('7','FOODTECH'),
    ('8','HARDWARE'),
)
class startUp(models.Model):
    name = models.TextField(max_length=30 )
    contactNo = models.IntegerField(max_length=10)
    email = models.EmailField()
    iitian = models.CharField(max_length=6,null=True, choices=IITian_choices)
    hostel = models.CharField(max_length=10, choices=Hostel_choices,null = True)
    startup_name = models.CharField(max_length=30)
    startup_sector = models.CharField(max_length=30, choices=Sector_choices, null=True)
    startup_desc = models.TextField(max_length=1000, default= 'description')
    comments = models.CharField(max_length=1000,null=True)
# Create your models here.
