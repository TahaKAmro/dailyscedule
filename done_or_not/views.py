from django.shortcuts import render
from .models import *
# Create your views here.
def mainpage(request):
    days = Day.objects.order_by('-date')
    return render(request , 'done_or_not/mainpage.html'  ,{
        'page_name':'Home',
        'day':days , 
})