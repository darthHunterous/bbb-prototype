from django.shortcuts import render, redirect
from .forms import PollForm

def index(request):
    form = PollForm()
    context = { 'form': form }

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

    context = { 'data': data }

    return render(request, 'polling/poll.html', context)