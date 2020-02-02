from django.shortcuts import render
from  django.http import HttpResponse
def home(request):
	return render(request,'home.html',{'name':'akhil'})

def add(request):
	var1=request.POST["num1"]
	var2=request.POST["num2"]
	if (var1==var2=="admin"):
		return render(request,'result.html',{'result':'success'})
	else:
		return render(request,'result.html',{'result':'failed'})
# Create your views here.
