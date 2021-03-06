from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    year_of_birth = models.IntegerField()
    student_id = models.IntegerField(unique=True)
    group = models.ForeignKey("group.Group")

    def __str__(self):
        return self.last_name
