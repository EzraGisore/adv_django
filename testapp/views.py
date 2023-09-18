from django.http import HttpResponse
from django.shortcuts import render

# Create your views he
def home(request):
    return render(request,'index.html')
