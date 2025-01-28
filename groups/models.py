from django.db import models
from subjects.base_model import BaseModel
from teachers.models import Teacher
from django.shortcuts import reverse


class Group(BaseModel):
    name = models.CharField(max_length=50)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name='groups')

    def __str__(self):
        return self.name

    def get_detail_url(self):
        return reverse('groups:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('groups:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('groups:delete', args=[self.pk])