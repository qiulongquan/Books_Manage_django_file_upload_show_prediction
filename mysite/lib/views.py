# mysite/lib/views.py
from django.shortcuts import render
from .models import Book
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone


def process(request):
    if request.method == 'POST':
        if 'button_1' in request.POST:
            # ボタン1がクリックされた場合の処理
            print("button_1")
            return HttpResponseRedirect(reverse('lib:detail'))
        elif 'button_2' in request.POST:
            # ボタン2がクリックされた場合の処理
            print("button_2")
            return HttpResponseRedirect(reverse('polls:question'))


def detail(request):
    book_list = Book.objects.order_by('-pub_date')[:5]
    context = {'book_list': book_list}
    return render(request, 'lib/detail1.html', context)


def addBook(request):
    if request.method == 'POST':
        temp_name = request.POST['name']
        temp_author = request.POST['author']
        temp_pub_house = request.POST['pub_house']

    from django.utils import timezone
    temp_book = Book(name=temp_name, author=temp_author, pub_house=temp_pub_house, pub_date=timezone.now())
    temp_book.save()

    #重定向
    return HttpResponseRedirect(reverse('lib:detail'))


def update_info(request,book_id):
    if request.method == 'POST':
        temp_name = request.POST['name']
        temp_author = request.POST['author']
        temp_pub_house = request.POST['pub_house']

    from django.utils import timezone
    Book.objects.filter(id=book_id).update(name=temp_name,author=temp_author,pub_house=temp_pub_house,pub_date=timezone.now())
    #重定向
    return HttpResponseRedirect(reverse('lib:detail'))


def delBook(request,book_id):
    bookID = book_id
    Book.objects.filter(id=bookID).delete()
    # 重定向
    return HttpResponseRedirect(reverse('lib:detail'))




