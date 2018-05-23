import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core import serializers

from .models import Answer
from .forms import AnswerForm

def own_answers(request):
    answer_ids = request.COOKIES.get("answer-ids", None)
    if answer_ids is not None and len(answer_ids) > 0:
        ids = set(map(int, answer_ids.split(",")))
    else:
        ids = set()
    if "answer-id" in request.COOKIES:
        ids.add(int(request.COOKIES["answer-id"]))
    return ids

def index(request):
    answers = Answer.objects.all()
    total_count = sum(answer.count for answer in answers)
    context = {
               "answers": answers,
               "total_count": total_count,
               "own_answers": own_answers(request),
              }
    return render(request, 'polls/index.html', context)

def json_summary(request):
    answers = Answer.objects.all()
    return HttpResponse(serializers.serialize('json', answers), content_type="application/json")


def add_answer(request):
    if request.method == "GET":
        form = AnswerForm()
    elif request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            response = redirect("index")
            answer_ids = own_answers(request)
            answer_ids.add(answer.id)
            response.set_cookie("answer-ids", ",".join(map(str, answer_ids)))
            return response
    return render(request, 'polls/add_answer.html', {"form": form})

def del_answer(request, answer_id):
    answer_id = int(answer_id)
    answer = Answer.objects.get(id=answer_id)
    answer.delete()
    response = redirect("index")
    if request.COOKIES.get("answer-id", None) == str(answer_id):
        response.delete_cookie("answer-id")
    response.set_cookie("answer-ids", ",".join(map(str, own_answers(request) - {answer_id})))
    return response
