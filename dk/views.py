from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpRequest
from .ser.req import dely
from django.template.response import TemplateResponse
from django.shortcuts import loader
from dk import models
import json


def pr(request, year=None):
    print(request)
    dd = models.Person.objects.all()
    print(list(dd.values()))
    # models.Person.objects.create(first_name='pi', last_name='wenwen')
    # 上面代码不写默认的id时，必须书写键值对
    # kk = dd.get(id=1)
    # kk.first_name = 'dkwx'
    # kk.save()
    # kk = models.Person(id=1, first_name='dk', last_name='Tom')
    # models.Person.objects.create(id=5, first_name='wen', last_name='xue')
    # kk.save()
    # kkk = dd.values('id', 'first_name', 'last_name').order_by('first_name')
    # print(list(kkk))
    kkk = dd.values_list('id', 'first_name')
    print(list(kkk))
    print(list(kkk)[0][1])
    # for k in list(kkk):
    #     print(k)
    con = {
        'name': 'dk',
        'age': 24,
        'sex': {
            'time': '2017-2',
            'date': '星期二'
        },
        'var01': '',
        'var02': '',
        'im': '<strong>星期二</strong>',
        'cities': [
            {'name': 'Mumbai', 'population': '19,000,000', 'country': 'India'},
            {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
            {'name': 'Calcutta', 'population': '15,000,000', 'country': 'India'},
            {'name': 'Chicago', 'population': '7,000,000', 'country': 'USA'},
            {'name': 'Tokyo', 'population': '33,000,000', 'country': 'Japan'},
        ],
        'value': "i'm sorry for that",
        'value1': "django",
        'cutValue': 'This aaaaaais TOM',
        'dict_list': [
            {'name': 'zed', 'age': 3},
            {'name': 'amy', 'age': 1},
            {'name': 'joe', 'age': 2},
        ],
        'list_join': ['a', 'b', 'c'],
        'under_l': ['States', ['Kansas', ['Lawrence', 'Topeka'], 'Illinois']],
        'year': year,
    }
    # con = dely(year)
    # return render(request, 'bm.html', context=con, status=200)
    # return TemplateResponse(request, 'bm.html', context=con, status=200)
    # t = loader.render_to_string('bm.html', con, request)
    return HttpResponse(loader.render_to_string('bm.html', context=con))
    # return HttpResponse(t)


# def page_not_found(request):
#     return render(request, '404.html')

def pp(request):
    return HttpResponse("<h1>Welcome to First Page</h1>")


def dd(request, username=None):
    return HttpResponse(username)



