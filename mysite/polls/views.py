from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import Http404

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
# normal way try catch?
  try:
    question = Question.objects.get(pk=question_id)
  except Question.DoesNotExist:
    raise Http404("Question does not exist")
  context = {'question': question}
  return render(request, 'polls/detail.html', context)

def results(request, question_id):
# using get_object_or_404() shortcut
  question = get_object_or_404(Question, pk=question_id)
  context = {'question': question}
  return render(request, 'polls/results.html', context)

def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  context = {'question': question}
  return render(request, 'polls/vote.html', context)
