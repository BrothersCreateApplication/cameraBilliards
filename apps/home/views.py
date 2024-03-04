from django.shortcuts import render

# Create your views here.


def policy(request):
    return render(request, 'policy/index.html')


def termsofuse(request):
    return render(request, 'terms-of-use/index.html')


def support(request):
    return render(request, 'support/index.html')
