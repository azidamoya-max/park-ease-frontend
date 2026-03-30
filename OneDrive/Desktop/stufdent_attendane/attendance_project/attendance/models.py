from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    is_present = models.BooleanField(default=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.student_id})"