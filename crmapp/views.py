from django.shortcuts import render
import mysql.connector


con = mysql.connector.connect(host = 'localhost', user = 'root', password = 'Hailmary@12345.', database = 'crmbase')
cursor = con.cursor()

# Create your views here.
