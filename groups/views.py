from django.shortcuts import render, redirect, get_object_or_404

from students.models import Student
from teachers.models import Teacher
from .models import Group


def group_list(request):
    groups = Group.objects.all()
    ctx = {'groups': groups}
    return render(request, 'groups/groups-list.html', ctx)

def group_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        teacher = request.POST.get('teacher')
        if name and teacher:
            teacher = Teacher.objects.get(id=teacher)
            Group.objects.create(
                name = name,
                teacher = teacher,
            )
            return redirect('groups:list')
    teachers = Teacher.objects.all()
    ctx = {'teachers': teachers}
    return render(request,'groups/group-add.html', ctx)

def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    students = Student.objects.filter(group=group)
    ctx = {'group': group, 'students':  students}
    return render(request, 'groups/group-detail.html', ctx)

def group_update(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        teacher = request.POST.get('teacher')
        if name and teacher:
            teacher = Teacher.objects.get(id=teacher)
            group.name = name
            group.teacher = teacher
            group.save()
            return redirect('groups:list')
    teachers = Teacher.objects.all()
    ctx = {'teachers': teachers, 'group': group}
    return render(request, 'groups/group-add.html', ctx)

def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    group.delete()
    return redirect('groups:list')


