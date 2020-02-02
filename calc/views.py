from django.shortcuts import render
from  django.http import HttpResponse
def home(request):
	return render(request,'home.html',{'name':'akhil'})

def add(request):
	var1=request.POST["num1"]
	var2=request.POST["num2"]
	res=int(var1)+int(var2)
	return render(request,'result.html',{'result':res})
# Create your views here.
