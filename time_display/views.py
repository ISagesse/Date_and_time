from django.shortcuts import render
from datetime import datetime

today_time = datetime.today()

# Create your views here.

def time(request):
    context = {
        "date": datetime.strftime(today_time, "%Y-%m-%d"),
        "time": datetime.strftime(today_time, "%I:%M %p")
    }
    return render(request, 'index.html', context)
