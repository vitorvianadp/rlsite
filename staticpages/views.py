from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'staticpages/index.html', context)


def about(request):
    context = {}
    return render(request, 'staticpages/about.html', context)

def theory(request):
    context = {}
    return render(request, 'staticpages/theory.html', context)

def algorithms(request):
    context = {}
    return render(request, 'staticpages/algorithms.html', context)