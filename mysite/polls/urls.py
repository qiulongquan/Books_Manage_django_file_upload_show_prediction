# polls/urls.py
from django.urls import path
from . import questions
from . import choice

#添加这行 命名空间
app_name = 'polls'

urlpatterns = [
    path('question/', questions.question, name='question'),
    # path('detail/', views.detail, name='detail'),
    # path('process/', views.process, name='process'),
    path('addQuestion/', questions.addQuestion, name='addQuestion'),
    path('choice/', questions.choice, name='choice'),
    path('replyQuestion/<int:question_id>', questions.replyQuestion, name='replyQuestion'),
    # path('updateBook/<int:book_id>', views1.updateBook, name='updateBook'),
    path('delQuestion/<int:question_id>', questions.delQuestion, name='delQuestion'),
]