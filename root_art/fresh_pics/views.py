from django.shortcuts import render


def fresh_home(request):
    return render(request, 'fresh_pics/fresh_home.html')

