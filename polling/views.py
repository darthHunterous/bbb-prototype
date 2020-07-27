from django.shortcuts import render, redirect

from .models import Question	
from .forms import PollForm

def index(request):
    polls = Question.objects.order_by('id')	

    context = { 'polls': polls }
    
    return render(request, 'polling/index.html', context)

def poll(request):
    if request.method == "POST":
        data = []
        if request.POST['option01'] != '':
            data.append(request.POST['option01'])
        if request.POST['option02'] != '':
            data.append(request.POST['option02'])
        if request.POST['option03'] != '':
            data.append(request.POST['option03'])
        if request.POST['option04'] != '':
            data.append(request.POST['option04'])
        if request.POST['option05'] != '':
            data.append(request.POST['option05'])
    else:
        options = request.GET.get("options")
        if options == 'yn':
            data = ["Yes", "No"]
        if options == 'tf':
            data = ["True", "False"]
        if options == 'ab':
            data = ["A", "B"]
        if options == 'abc':
            data = ["A", "B", "C"]
        if options == 'abcd':
            data = ["A", "B", "C", "D"]
        if options == 'abcde':
            data = ["A", "B", "C", "D", "E"]
        if options == 'txt':
            data = []

    context = { 'data': data }

    return render(request, 'polling/poll.html', context)

### tutorial below	
def detail(request, question_id):	
    return HttpResponse("You're looking at question %s." % question_id)	

def results(request, question_id):	
    response = "You're looking at the results of question %s."	
    return HttpResponse(response % question_id)	

def vote(request, question_id):	
    return HttpResponse("You're voting on question %s." % question_id) 