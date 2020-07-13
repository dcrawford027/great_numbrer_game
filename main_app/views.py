from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if 'answer' not in request.session:
        request.session['answer'] = random.randint(1, 100)
    context = {
        'answer': request.session['answer'],
    }
    if 'userNum' in request.session:
        if int(request.session['userNum']) > request.session['answer']:
            context['correct'] = False
            context['low'] = False
            context['high'] = True
        elif int(request.session['userNum']) < request.session['answer']:
            context['correct'] = False
            context['high'] = False
            context['low'] = True
        else:
            context['high'] = False
            context['low'] = False
            context['correct'] = True
    print(context)
    return render(request, 'index.html', context)

def guess(request):
    userNum = request.POST['guess']
    request.session['userNum'] = userNum
    return redirect('/')

def start(request):
    del request.session['answer']
    del request.session['userNum']
    return redirect('/')