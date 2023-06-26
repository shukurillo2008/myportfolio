from main import models
from django.shortcuts import render, redirect

def index(request):
    me = models.AboutMe.objects.all().last()
    social = models.Social.objects.all()
    indicator = models.IndicatorWin.objects.all().last()
    skill = models.MySkills.objects.all()
    interest = models.Hobby.objects.all()
    comment = models.ClientComment.objects.all()
    history = models.History.objects.all()
    service = models.MyServise.objects.all()
    category = models.CategoryWork.objects.all()
    work = models.MyWork.objects.all()
    
    context = {
        "me":me,
        "ind":indicator,
        "skill":skill,
        'hobby':interest,
        "comment":comment,
        "history":history,
        "service":service,
        "category":category,
        "work":work,
        "social":social
    }

    return render(request, 'index.html', context)


def portfolio(request, id):
    work = models.MyWork.objects.get(id = id)
    workimage = models.MyWorkImage.objects.filter(work = work)
    
    context ={
        "work" : work,
        "workimage" : workimage
    }

    return render(request, 'portfolio-details.html', context)