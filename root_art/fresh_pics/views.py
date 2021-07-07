from django.shortcuts import render
from .models import Pictures


def fresh_home(request):
    categories = Pictures.objects.all()
    return render(request, 'fresh_pics/fresh_home.html', {'categories': categories})
