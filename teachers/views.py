from django.shortcuts import render, redirect, get_object_or_404
from subjects.models import Subject
from .models import Teacher

def teacher_list(request):
    teachers = Teacher.objects.all()
    ctx = {'teachers': teachers}
    return render(request,'teachers/teachers-list.html', ctx)

def teacher_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        work_experience = request.POST.get('work_experience')
        image = request.FILES.get('image')
        if first_name and last_name and subject and phone and email and work_experience and image:
            subject = Subject.objects.get(id=subject)
            Teacher.objects.create(
                first_name = first_name,
                last_name = last_name,
                subject = subject,
                phone = phone,
                email = email,
                work_experience = work_experience,
                image = image,
            )
            return redirect('teachers:list')
    subjects = Subject.objects.all()
    ctx = {'subjects': subjects}
    return render(request,'teachers/teacher-add.html', ctx)

def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    ctx = {'teacher': teacher}
    return render(request,'teachers/teacher-detail.html', ctx)

def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        work_experience = request.POST.get('work_experience')
        image = request.FILES.get('image')
        if first_name and last_name and subject and phone and email and work_experience and image:
            subject = Subject.objects.get(id=subject)
            teacher.first_name = first_name
            teacher.last_name = last_name
            teacher.subject = subject
            teacher.phone = phone
            teacher.email = email
            teacher.work_experience = work_experience
            if image:
                teacher.image = image
            teacher.save()
            return redirect('teachers:list')
    subjects = Subject.objects.all()
    ctx = {'subjects': subjects, 'teacher': teacher }
    return render(request,'teachers/teacher-add.html', ctx)

def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    teacher.delete()
    return redirect('teachers:list')