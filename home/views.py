from django.shortcuts import render, HttpResponse
from datetime import datetime
 
from django.contrib import messages


# Create your views here.
def index(request):
       
        return render(request,'index.html')
    

def temp_c(request):
    if request.method == 'POST':
        t = request.POST['t']
        if t=='':
            return render(request,'temp.html')
        else:
            if 'cf' in request.POST:
               result = cf(t)
               return render(request,'temp.html',{'result':result})
        
            elif 'ck' in request.POST:
              result =  ck(t)
              return render(request,'temp.html',{'result':result})
 
            elif 'div' in request.POST:
              result =  fc(t)
              return render(request,'temp.html',{'result':result})
 
            elif 'mul' in request.POST:
                result =  kc(t)
                return render(request,'temp.html',{'result':result})
    
            else:
              return render(request,'temp.html')
          
          
    return render(request,'temp.html')


def cf(t):
    t=int(t)
    r=(t*9/5)+32
    return f"{t}C={r}F"
def ck(t):
    t=int(t)
    r=t+273.15
    return f"{t}C={r}K"
def fc(t):
    t=int(t)
    r= (t-32)*5/9
    return f"{t}F={r}C"
def kc(t):
    t=int(t)
    r=t-273.15
    return f"{t}K={r}C"

 
def Addition(num1,num2):
    result = int(num1) + int(num2)
    return f"{num1}+{num2}={result}"
 
def Subtract(num1,num2):
    result = int(num1) - int(num2)
    return f"{num1}-{num2}={result}"
 
def Divide(num1,num2):
    result = int(num1) / int(num2)
    return  f"{num1}/{num2}={result}"
 
def Multiply(num1,num2):
    result = int(num1) * int(num2)
    return  f"{num1}*{num2}={result}"


def calculator(request):
    if request.method == 'POST':
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        if num1==''or num2=='':
            return render(request,'calculator.html')
        else:
          if 'add' in request.POST:
            result = Addition(num1,num2)
            return render(request,'calculator.html',{'result':result})
        
          if 'sub' in request.POST:
            result = Subtract(num1,num2)
            return render(request,'calculator.html',{'result':result})
 
          if 'div' in request.POST:
            result = Divide(num1,num2)
            return render(request,'calculator.html',{'result':result})
 
          if 'mul' in request.POST:
            result = Multiply(num1,num2)
            return render(request,'calculator.html',{'result':result})
    return render(request,'calculator.html')