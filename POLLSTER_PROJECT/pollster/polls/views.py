from django.shortcuts import render

# Create your views here.
from .models import Question, Choice 

# Get questions and display them 
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5] 
    context = {'latest_question_list':latest_question_list}
    return render(request,'polls/index.html',context)

# Show Specific question and choices
def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question Does Not Exist")
    return render(request,'polls/results.html',{'question': question})

# Get Question and display Results
def results(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/results.html',{'question':question})
