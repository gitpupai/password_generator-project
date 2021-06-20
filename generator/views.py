from django.shortcuts import render
from django.http import HttpResponse
import random #used to generate random password

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def randomcode(request):
    return HttpResponse(" Check urls.py file, add a path to it, give a function call with name randomcode, \n This code running from randomcode func,\n We need to import HttpResponse from django.http\n")

def templatestake(request):
    return render(request, 'generator/templatestake.html',{'password': '00hsgd333'}) #look for home.html file and add password dictionary to it

def func_password(request):
    return render(request, 'generator/password.html')

def func_about(request):
    return render(request,'generator/about_page.html')

def func_passgen(request):
    pwd=''
    while len(pwd)<12:
        chars=list('abcdefghijklmnopqrstuvwxyz')
        nums=list('1234567890')
        char=random.choice(chars)
        num=random.choice(nums)
        charnum=char+num
        randcharnum=random.choice(charnum)
        pwd+=randcharnum
    the_password=pwd
    return render(request, 'generator/Goto.html',{'password':the_password})

def func_passgen2(request):
    chars=list('abcdefghijklmnopqrstuvwxyz')
    the_password=''
    onlyupper=''
    onlynum=''
    nums='1234567890'
    the_length=int(request.GET.get("length",'8'))

    if request.GET.get("uppercase"):#same spelling as in password.html file
        chars.extend(''.join(chars).upper())
        onlyupper='upper'
    if request.GET.get("numbers"):
        chars.extend(nums)
        onlynum='num'


    upper_check=True
    num_check=True
    while num_check or upper_check:
        for item in range(the_length):
            the_password+=random.choice(chars)

        if onlyupper=='upper': #at least one uppercase
            for char in the_password:
                if char.isupper():
                    upper_check=False
            if upper_check!=False: #no uppercase
                the_password='' #start again
        else:
            upper_check=False

        if onlynum=='num': #at least one number
            for char in the_password:
                if char.isdigit():
                    num_check=False
            if num_check!=False: #no numbers
                the_password='' #start again
        else:
            num_check=False
    return render(request, 'generator/Goto.html',{'password':the_password})
