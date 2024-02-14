from django.shortcuts import render

# Create your views here.
import datetime


def filters(request):
    dt=datetime.datetime.now()
    d={'data':'I aM vErY InteLLigeNt GiRL','date' :dt,'c':0}
    return render(request,'filters.html',d)

def userDfilters(request):
    d1={'data':'DjanGO Is AlmoSt ComPleTeD'}
    return render(request,'userDfilters.html',d1)