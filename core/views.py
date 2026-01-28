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
    return render(request, 'home.html',context)


# Create your views here.
