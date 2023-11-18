from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'staticpages/index.html', context)


def theory(request):
    context = {}
    return render(request, 'staticpages/theory.html', context)

def e_greedy(request):
    context = {}
    return render(request, 'staticpages/e_greedy.html', context)

def greedy(request):
    context = {}
    return render(request, 'staticpages/greedy.html', context)

def ucb(request):
    context = {}
    return render(request, 'staticpages/ucb.html', context)