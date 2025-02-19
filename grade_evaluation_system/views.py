from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import django.contrib.messages as messages
from django.db.models import Q
import csv


from .models import Grade


def home(request):
    """The home page for Student Evaluation System"""
    return render(request, 'grade_evaluation_system/home.html')


@login_required
def grade_evaluation(request):
    """Shows the all the students grade evaluation"""
    grades = Grade.objects.all()
    context = {'grades': grades}
    
    return render(request, 'grade_evaluation_system/grade_evaluation.html', context)


@login_required
def search_grade(request):
    """Shows the searched grade"""
    if request.method == "POST":
        searched = request.POST['searched']
        # the student_number is the variable name of the foriegn key and the other one is the name of the primary key
        grades = Grade.objects.filter(Q(student_number__icontains=searched) | Q(subject__subject_name__icontains=searched) | Q(course__course__icontains=searched))

        if not searched:
            messages.error(request, "doesn't exist")
            return render(request, 'grade_evaluation_system/search_grade.html', {})

        context = {'searched': searched, 'grades': grades}

        return render(request, 'grade_evaluation_system/search_grade.html', context)
    
    else:
        context = {"error": "Please Enter what you want to search"}
        return render(request, 'grade_evaluation_system/search_grade.html', context)

@login_required
def show_1st_semester(request):
    """Shows the 1st semester in the dropdown"""
    grades = Grade.objects.filter(semester__contains=1)
    context = {'grades': grades}

    return render(request, 'grade_evaluation_system/semester1.html', context)

@login_required
def show_2nd_semester(request):
    """Shows the 2nd semester in the dropdown"""
    grades = Grade.objects.filter(semester__contains=2)
    context = {'grades': grades}

    return render(request, 'grade_evaluation_system/semester2.html', context)

