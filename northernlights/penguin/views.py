from django.shortcuts import render
from datetime import datetime

def index(request):
    return render(request, 'index.html')

def exercise(request):
    text = 'テストです。'
    try:
        input_text = request.POST['input_text']
        print(input_text)
        text = input_text
    except:
        return render(request, 'exercise.html')

    now = datetime.now();
    context = {
        'text': text,
        'time': now,
    }
    return render(request, 'exercise.html', context)
