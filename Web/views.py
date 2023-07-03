from django.shortcuts import render


def homepage(request):
    return render(request, "Web/Index.html")
