from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import FiboForm
from decimal import Decimal
import time

# Create your views here.
fibonacci_series=[0,1]

def fib(n):
    for i in range(2, n+1):
        fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])
    return fibonacci_series[n]
@csrf_exempt
def fibonacci(request) :
    result=0
    reqTime=""
    n=""
    if request.method == 'POST':
        reqTime=lambda: int(round(time.time() * 1000))
        print(reqTime)
        form = FiboForm(request.POST)
        if form.is_valid():
            n=form.cleaned_data['n']
            result=fib(int(n))
            if(len(str(result))>20):
                result="HEX: " + str(hex(result))
        print(reqTime)
        return render(request, 'fibo.html', {'form': form,'result':result,'reqTime':reqTime,'n':n})
    else :
        form = FiboForm()
        return render(request, 'fibo.html', {'form': form,'result':result,'reqTime':reqTime})
