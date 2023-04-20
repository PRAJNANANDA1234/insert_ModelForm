from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.
def inset_topic(request):
    TOF=Topicform()
    d={'TOF':TOF}
    if request.method=='POST':
        TFD=Topicform(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('topic is  insrted successfully')


    return render(request,'insert_topic.html',d)

def inset_webpage(request):
    WOF=Webpageform()
    d={'WOF':WOF}
    if request.method=='POST':
        WFD=Webpageform(request.POST)
        if WFD.is_valid():
            WFD.save()
            return HttpResponse('webpage is  insrted successfully')


    return render(request,'insert_webpage.html',d)

def inset_accessrecord(request):
    AOF=Accessrecordform()
    d={'AOF':AOF}
    if request.method=='POST':
        AFD=Accessrecordform(request.POST)
        if AFD.is_valid():
            AFD.save()
            return HttpResponse('accessrecord is  insrted successfully')


    return render(request,'insert_accessrecord.html',d)