from django.shortcuts import render
from django.views import View
from staticapp.forms import InputForm
from staticapp.models import table
from django.http import HttpResponse

class Home(View):
    def get(self,request):
        return render(request,'Home.html')

class Input(View):
    def get(self,request):
        frm=InputForm
        return render(request,'Input.html',{'frm':frm})

class Insert(View):
    def post(self,request):
        obj=InputForm(request.POST)
        if obj.is_valid():
            obj.save()
        return HttpResponse("Data Submitted")