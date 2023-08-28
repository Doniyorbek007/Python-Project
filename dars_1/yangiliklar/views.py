from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def yangiliklar(req):
    return render(req, 'index.html')

def yangilik(req):
    if id > 0 and id < 4:
        yangiliklar_ = [
            'yangilik 1',
            'yangilik 2',
            'yangilik 3',
        ]
        return HttpResponse(yangiliklar_[id-1])
    else:
        return HttpResponse('Bunday yangilik mavjud emas')

# def ozgartirish(req):
#     return render(req, )