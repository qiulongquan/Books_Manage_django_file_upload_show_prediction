# lib/urls.py
from django.urls import path
from . import views1
from . import views

#添加这行 命名空间
app_name = 'lib'

urlpatterns = [
    path('', views1.index, name='index'),
    path('index/', views1.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('process/', views.process, name='process'),
    path('addBook/', views.addBook, name='addBook'),
    path('update_info/<int:book_id>', views.update_info, name='update_info'),
    path('updateBook/<int:book_id>', views1.updateBook, name='updateBook'),
    path('delBook/<int:book_id>', views.delBook, name='delBook'),
]
