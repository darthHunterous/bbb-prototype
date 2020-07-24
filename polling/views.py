from django.shortcuts import render


def index(request):
    context = {}

    return render(request, 'polling/index.html', context)