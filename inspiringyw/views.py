from django.shortcuts import render


def handler404(request, exception):
    """ 404 ERROR page """
    return render(request, '404.html', status=404)


def handler500(request):
    """ 500 ERROR page """
    return render(request, '500.html', status=500)
