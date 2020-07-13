from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if 'answer' not in request.session:
        request.session['answer'] = random.randint(1, 100)
        request.session['counter'] = 0
    context = {}
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
    print(request.session['counter'])
    return render(request, 'index.html', context)

def guess(request):
    userNum = request.POST['guess']
    request.session['userNum'] = userNum
    request.session['counter'] += 1
    return redirect('/')

def start(request):
    del request.session['answer']
    if 'userNum' in request.session:
        del request.session['userNum']
    return redirect('/')