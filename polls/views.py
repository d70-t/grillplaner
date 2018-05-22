from django.shortcuts import render, redirect

from .models import Answer
from .forms import AnswerForm

def index(request):
    answers = Answer.objects.all()
    total_count = sum(answer.count for answer in answers)
    my_answer_id = request.COOKIES.get("answer-id", None)
    if my_answer_id is not None:
        my_answer_id = int(my_answer_id)
    context = {
               "answers": answers,
               "total_count": total_count,
               "my_answer_id": my_answer_id,
              }
    return render(request, 'polls/index.html', context)

def add_answer(request):
    if request.method == "GET":
        form = AnswerForm()
    elif request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            response = redirect("index")
            response.set_cookie("answer-id", answer.id)
            return response
    return render(request, 'polls/add_answer.html', {"form": form})

def del_answer(request, answer_id):
    answer_id = int(answer_id)
    answer = Answer.objects.get(id=answer_id)
    answer.delete()
    response = redirect("index")
    response.delete_cookie("answer-id")
    return response
