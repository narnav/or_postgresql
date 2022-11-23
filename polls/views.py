from django.http import HttpResponse
from django.shortcuts import render
from polls.models import Question

def index(request):
    quest= Question(question_text="desccc",pub_date="dateee")
    quest.save()
    res = []
    questions=Question.objects.all()
    for question in questions:
        res.append(question.question_text)
    return HttpResponse(res)