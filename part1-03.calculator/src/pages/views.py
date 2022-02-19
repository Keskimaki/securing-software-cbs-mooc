from django.http import HttpResponse


def addPageView(request):
    first = int(request.GET.get('first'))
    second = int(request.GET.get('second'))

    return HttpResponse(first + second)	

def multiplyPageView(request):
    first = int(request.GET.get('first'))
    second = int(request.GET.get('second'))

    return HttpResponse(first * second)
