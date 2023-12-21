from django.shortcuts import render
import mysql.connector


con = mysql.connector.connect(host = 'localhost', user = 'root', password = 'Hailmary@12345.', database = 'crmbase')
cursor = con.cursor()

def index(request):
    
    return render(request, 'index.html', {})

# Create your views here.
