# mysite/polls/questions.py
from django.shortcuts import render, resolve_url
from .models import Question
from .models import Choice
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone


def question(request):
    question_list = Question.objects.order_by('-pub_date')[:]
    context = {'question_list': question_list}
    return render(request, 'polls/question.html', context)


def replyQuestion(request, question_id):
    questionID = question_id
    # print("qiulongquan_questionID={}".format(questionID))
    # 只返回一条记录的时候用get，返回结果可以直接读取不需要for
    question_info = Question.objects.get(id=questionID)
    # 返回多条或者一条记录的时候用filter，但是返回结果要用for循环来读取
    choice_info = Choice.objects.filter(question_id=questionID)
    # print("qiulongquan_question_info={},{}".format(question_info.question_text, question_info.pub_date))
    context = {'question_info': question_info, 'choice_info': choice_info}
    return render(request, 'polls/choice.html', context)


def delQuestion(request, question_id):
    questionID = question_id
    Question.objects.filter(id=questionID).delete()
    # 重定向
    return HttpResponseRedirect(reverse('polls:question'))


def addQuestion(request):
    if request.method == 'POST':
        question_text = request.POST['question_text']

    from django.utils import timezone
    temp_question = Question(question_text=question_text, pub_date=timezone.now())
    temp_question.save()

    #重定向redirect
    return HttpResponseRedirect(reverse('polls:question'))


def choice(request):
    if request.method == 'POST':
        question_id = request.POST['question_id']
        # print("qiulongquan_question_id={}".format(question_id))
        checkbox_status = request.POST.getlist('tags')
        # print("qiulongquan_checkbox_status={}".format(checkbox_status))
        temp_choice = Choice(choice_text=request.POST['choice_text'], votes=checkbox_status, question_id=request.POST['question_id'])
        temp_choice.save()

    #重定向redirect
    url = resolve_url('polls:replyQuestion', question_id)
    return HttpResponseRedirect(url)
