from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

from calc.controller.fun_controller import Controller

"""
def index(request):
    template = loader.get_template('calc/index.html')
    context = {
        'ans' : 123456789
    }
    return HttpResponse(template.render(context,request))
"""

def index(request):
    c = Controller()
    if('ans' in request.GET):
        sol = c.solucionador(request.GET['ans'])
    else:
        sol = ''
    return render(request, "calc/index.html", {"ans" : sol})
