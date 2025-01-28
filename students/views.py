from django.shortcuts import render, get_object_or_404, redirect
from groups.models import Group
from .models import Student


def student_list(request):
    students = Student.objects.all()
    ctx = {'students': students}
    return render(request,'students/students-list.html', ctx)

def student_create(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        group = request.POST.get('group')
        dob = request.POST.get('dob')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        image = request.FILES.get('image')
        if full_name and group and dob and phone and address and image:
            group = get_object_or_404(Group, id=group)
            Student.objects.create(
                full_name = full_name,
                group = group,
                dob = dob,
                phone = phone,
                address = address,
                image = image,
            )
            return redirect('students:list')
    groups = Group.objects.all()
    ctx = {'groups': groups}
    return render(request,'students/student-add.html', ctx)

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    ctx = {'student': student}
    return render(request,'students/student-detail.html', ctx)

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        group = request.POST.get('group')
        dob = request.POST.get('dob')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        image = request.FILES.get('image')
        if full_name and group and dob and phone and address and image:
            group = get_object_or_404(Group, id=group)
            student.full_name = full_name
            student.group = group
            student.dob = dob
            student.phone = phone
            student.address = address
            student.image = image
            student.save()
            return redirect('students:list')
    groups = Group.objects.all()
    ctx = {'groups': groups, 'student': student}
    return render(request, 'students/student-add.html', ctx)

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('students:list')
