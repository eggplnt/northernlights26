from django.shortcuts import render
from datetime import datetime

def index(request):
    return render(request, 'index.html')

def exercise(request):
    now = datetime.now();
    context = {
        'text': 'テストです。',
        'time': now,
    }
    return render(request, 'exercise.html', context)
