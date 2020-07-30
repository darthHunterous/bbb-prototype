from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import F
from .models import Question, User, Vote, Choice
from .forms import PollForm

def index(request):
    unlaunched_polls = Question.objects.filter(launched=False)
    launched_polls = Question.objects.filter(launched=True)
    users = User.objects.all()

    context = { 'unlaunched_polls' : unlaunched_polls, 'launched_polls': launched_polls, 'users': users, 'user_id': 1 }

    return render(request, 'polling/index.html', context)

def create(request):
    if request.method == "POST":
        form = PollForm(request.POST)

        if form.is_valid():

            # Se o anonymous_answers for 'on', significa True
            anonymous_answers_fixed=request.POST.get('anonymousAnswers', False)
            if (anonymous_answers_fixed != False):
                anonymous_answers_fixed = True
            fA = request.POST.get('freeAnswers', False)
            if (fA != False):
              fA = True

            new_question = Question(question_text=request.POST['title'],
                                    free_answers=fA,
                                    anonymous_answers=anonymous_answers_fixed)
            new_question.save()
            if(fA == False):
              if request.POST['option01'] != '':
                  new_question.choice_set.create(choice_text=request.POST['option01'])
              if request.POST['option02'] != '':
                  new_question.choice_set.create(choice_text=request.POST['option02'])
              if request.POST['option03'] != '':
                  new_question.choice_set.create(choice_text=request.POST['option03'])
              if request.POST['option04'] != '':
                  new_question.choice_set.create(choice_text=request.POST['option04'])
              if request.POST['option05'] != '':
                  new_question.choice_set.create(choice_text=request.POST['option05'])

        
        return redirect('index')
    else:
        form = PollForm()
        context = { 'form': form }

        return render(request, 'polling/create.html', context)

def launch(request, poll_id):
    poll = Question.objects.get(pk=poll_id)
    poll.launched = True
    poll.save()

    return redirect('index')

def unlaunch(request, poll_id):
    poll = Question.objects.get(pk=poll_id)
    poll.launched = False
    poll.save()

    return redirect('index')

def edit(request, poll_id):
    if request.method == "POST":
        form = PollForm(request.POST)

        if form.is_valid():
            poll = Question.objects.get(pk=poll_id)
            poll.delete()
            # Se o anonymous_answers for 'on', significa True
            anonymous_answers_fixed=request.POST.get('anonymousAnswers', False)
            if (anonymous_answers_fixed != False):
                anonymous_answers_fixed = True

            new_question = Question(question_text=request.POST['title'],
                                    free_answers=request.POST.get('freeAnswers', False),
                                    anonymous_answers=anonymous_answers_fixed)
            new_question.save()

            if request.POST['option01'] != '':
                new_question.choice_set.create(choice_text=request.POST['option01'])
            if request.POST['option02'] != '':
                new_question.choice_set.create(choice_text=request.POST['option02'])
            if request.POST['option03'] != '':
                new_question.choice_set.create(choice_text=request.POST['option03'])
            if request.POST['option04'] != '':
                new_question.choice_set.create(choice_text=request.POST['option04'])
            if request.POST['option05'] != '':
                new_question.choice_set.create(choice_text=request.POST['option05'])

        
        return redirect('index')
    else:
        poll = Question.objects.get(pk=poll_id)

        values = poll.choice_set.values()
        options = []
        for i in range(0, 5):
            options.append("")
        j = 0
        for value in values:
            options[j] = value['choice_text']
            j += 1

        form = PollForm(initial={
            'title': poll.question_text,
            'option01': options[0],
            'option02': options[1],
            'option03': options[2],
            'option04': options[3],
            'option05': options[4],
            'freeAnswers': poll.free_answers,
            'anonymousAnswers': poll.anonymous_answers,
            })

        form.fields['title'].value = 'oi'
        context = { 'poll': poll, 'form': form }

        return render(request, 'polling/edit.html', context)

def user(request, user_id):
    users = User.objects.all()
    launched_polls = Question.objects.filter(launched=True)
    answered_polls = []
    unanswered_polls = []

    for poll in launched_polls:
        answered = False
        for choice in poll.choice_set.all():
            for vote in choice.vote_set.all():
                if int(vote.user.id) == int(user_id):
                    answered_polls.append(poll)
                    answered = True
        if not answered:
            unanswered_polls.append(poll)

    context = { 'user_id': int(user_id), 'users': users, 'answered_polls': answered_polls, 'unanswered_polls': unanswered_polls }
    return render(request, 'polling/user.html', context)

def vote(request):
    user_id = request.GET.get("userID")
    choice_id = request.GET.get('choiceID')

    user = User.objects.filter(pk=user_id)[0]
    choice = Choice.objects.filter(pk=choice_id)[0]
    print(choice.question.total_votes)
    choice.question.total_votes +=1
    choice.question.save()
    voteToRegister = Vote(choice=choice, user=user)
    voteToRegister.save()
    
    return redirect('user/' + user_id)
