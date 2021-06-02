from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import os
def index(request):
    return HttpResponse("你是伟杰吗！")
def getversion(request):
    print(request.path)
    if os.path.exists(request.path) != True:
        print("进入")
        txt = open(r"C:\Users\admin\Desktop\1.txt",encoding="utf-8").readlines()

        print("slkd")

        print(txt)
        if(txt !=""):
            return HttpResponse(txt)

    return HttpResponse("不存在，沙雕！")
