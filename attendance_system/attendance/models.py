from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    class_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.student.name + " - " + str(self.date)