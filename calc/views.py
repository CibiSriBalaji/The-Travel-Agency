from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')
def result(request):
    val1 = request.POST["number1"]
    val2 = request.POST["number2"]
    res = int(val1) + int(val2)
    return render(request, 'result.html', {"result":res})