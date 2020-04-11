# lib/views.py
from django.shortcuts import render
from lib.models import Book
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.utils.timezone import localtime
# Create your views here.


def index(request):
    now = localtime(timezone.now())
    print("qiulongquan_now={}".format(now))  # コード内でnowをprintしてみる
    # 把要传递给index.html的内容全部放到context里面，做成字典类型，然后在index.html里面调用存储的值
    context = {'now': now, 'qiu': "customization"}
    return render(request, 'lib/index.html', context)


def updateBook(request, book_id):
    bookID = book_id
    book_list=Book.objects.filter(id=bookID)
    context = {'book_list': book_list}
    return render(request, 'lib/detail_update.html', context)
    # return HttpResponse("Hello, world!qlq"+str(book_id))
