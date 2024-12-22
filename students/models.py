from django.db import models
from django.shortcuts import  reverse

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    image = models.ImageField(upload_to='students_images/')

    def get_detail_url(self):
        return reverse('students:detail', args={self.pk})