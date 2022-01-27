from django.shortcuts import render

# Create your views here.


def satr(request):
    return render(request, 'main/base.html')
