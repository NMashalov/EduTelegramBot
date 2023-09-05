from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"




class Task(models.Model):
    week =  models.PositiveIntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test= models.OneToOneField(
        Test,
        on_delete=models.CASCADE,
        primary_key=True,
    )






