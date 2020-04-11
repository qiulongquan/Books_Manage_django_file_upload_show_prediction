# hello/urls.py
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'hello'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prediction/', views.prediction),
    path('upload/', views.uploadImg),
    path('show/', views.showImg),
    path('delete/', views.deleteImg),
]
