from django.db import models
from django.utils import timezone
from django.utils.timezone import localtime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.CharField(max_length=20)

    def __str__(self):
        return self.choice_text
