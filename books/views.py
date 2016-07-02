#-*- coding:utf-8 -*-
from django.shortcuts import render
import datetime
from books.models import Book

def hello(request):
    return render(request,'hello.html',{'hello':'hello world!!!'})

def current_datetime(request):
    current_date = datetime.datetime.now()
    return render(request,'current_datetime.html',locals())

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request,'future_time.html',locals())

def access_info(request):
    path = request.path
    host = request.get_host()
    full_path = request.get_full_path()
    secure = request.is_secure()
    return render(request,'access_info.html',locals())

def meta(request):
    values = request.META.items()
    values.sort()
    return render(request,'meta.html',locals())

def search_form(request):
    return render(request,'search_form.html')

def search(request):
    errors = []
    if 'q' in request.GET:
	q = request.GET['q']
	if not q:
 	    errors.append('Enter a search term.')
#搜索关键词超过20个则给一条错误信息
	elif len(q) > 20:
	    errors.append('Please enter at most 20 characters.')
	else:
	    books = Book.objects.filter(title__icontains=q)
            return render(request,'search_results.html',{'books':books, 'query':q})  
    return render(request,'search_form.html',{'errors':errors})


