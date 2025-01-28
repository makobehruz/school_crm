from django.db import models
from groups.models import Group
from subjects.base_model import BaseModel
from django.shortcuts import reverse


class Student(BaseModel):
    full_name = models.CharField(max_length=100)
    group = models.OneToOneField(Group, on_delete=models.CASCADE, related_name='students')
    dob = models.DateField()
    phone = models.CharField(max_length=13)
    address = models.TextField()
    image = models.ImageField(upload_to='student_images/')

    def __str__(self):
        return self.full_name

    def get_detail_url(self):
        return reverse('students:detail',  args=[self.pk])

    def get_update_url(self):
        return reverse('students:update',  args=[self.pk])

    def get_delete_url(self):
        return reverse('students:delete',  args=[self.pk])