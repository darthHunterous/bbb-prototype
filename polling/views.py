from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Question	
from .forms import PollForm

def index(request):
    polls = Question.objects.order_by('id')
    context = { 'polls': polls }

    return render(request, 'polling/index.html', context)

def create(request):
    if request.method == "POST":
        form = PollForm(request.POST)

        if form.is_valid():
            # Se o anonymous_answers for 'on', significa True
            anonymous_answers_fixed=request.POST.get('anonymousAnswers', False)
            if (anonymous_answers_fixed != False):
                anonymous_answers_fixed = True

            new_question = Question(question_text=request.POST['title'],
                                    free_answers=request.POST.get('freeAnswers', False),
                                    anonymous_answers=anonymous_answers_fixed)
            new_question.save()

            if request.POST['option01'] != '':
                new_question.choice_set.create(choice_text=request.POST['option01'],
                                               votes=0)
            if request.POST['option02'] != '':
                new_question.choice_set.create(choice_text=request.POST['option02'],
                                               votes=0)
            if request.POST['option03'] != '':
                new_question.choice_set.create(choice_text=request.POST['option03'],
                                               votes=0)
            if request.POST['option04'] != '':
                new_question.choice_set.create(choice_text=request.POST['option04'],
                                               votes=0)
            if request.POST['option05'] != '':
                new_question.choice_set.create(choice_text=request.POST['option05'],
                                               votes=0)

        
        return redirect('index')
    else:
        form = PollForm()
        context = { 'form': form }

        return render(request, 'polling/create.html', context)

def view(request):

    context = { 'data': data }

    return render(request, 'polling/view.html', context)

### tutorial below	
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)	

def results(request, question_id):	
    response = "You're looking at the results of question %s."	
    return HttpResponse(response % question_id)	

def vote(request, question_id):	
    return HttpResponse("You're voting on question %s." % question_id) 
