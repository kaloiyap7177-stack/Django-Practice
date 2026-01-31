from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    name = "Pardeep"
    age = 20
    Skill = ['Python', 'Django', 'HTML']
    context = {
        'Username': name,
        'Skill_List': Skill,
        'Age': age,
    }
    return render(request, 'core/home.html',context)

def about(request):
    return render(request, "core/about.html")


# Create your views here.
