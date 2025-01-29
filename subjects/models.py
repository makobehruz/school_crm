from django.db import models
from .base_model import BaseModel
from django.shortcuts import reverse

class Subject(BaseModel):
    STATUS_CHOICES =[
        ('df', 'Draft'),
        ('pd', 'Published'),
    ]
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])

    def __str__(self):
        return self.name

    def get_detail_url(self):
        return reverse('subjects:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('subjects:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('subjects:delete', args=[self.pk])
