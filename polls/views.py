from django.shortcuts import render
import datetime
# Create your views here.
from django.http import HttpResponse

def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)