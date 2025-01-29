from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject
from teachers.models import Teacher
from students.models import Student
from groups.models import Group


def home(request):
    ctx = {
        'teachers_count': Teacher.objects.count(),
        'students_count': Student.objects.count(),
        'group_count': Group.objects.count(),
        'subjects_count': Subject.objects.count(),

    }
    return render(request,'index.html', ctx)


def subject_list(request):
    subjects = Subject.objects.all()
    ctx = {
        'subjects': subjects,
        'teachers_count': Teacher.objects.count(),
    }
    for subject in subjects:
        subject.teachers_count = Teacher.objects.filter(subject=subject).count()
    return render(request, 'subjects/subjects-list.html', ctx)


def subject_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Subject.objects.create(
                name = name,
            )
            return redirect('subjects:list')
    return render(request,'subjects/subject-add.html')

def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    teachers = Teacher.objects.filter(subject=subject)
    teachers_count = teachers.count()
    ctx = {
        'subject': subject,
        'teachers': teachers,
        'teachers_count': teachers_count,
    }
    return render(request, 'subjects/subject-detail.html', ctx)

def subject_update(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            subject.name = name
            subject.save()
            return redirect('subjects:list')
    ctx = {'subject': subject}
    return render(request,'subjects/subject-add.html', ctx)

def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    subject.delete()
    return redirect('subjects:list')