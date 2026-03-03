from django.db import models

# Create your models here.


class Students(models.Model):
    student_name = models.CharField(max_length=50)
    roll_no = models.IntegerField()
    tamil_mark = models.IntegerField()
    english_mark = models.IntegerField()
    maths_mark = models.IntegerField()
    science_mark = models.IntegerField()
    social_mark = models.IntegerField()
    total = models.PositiveSmallIntegerField()
    percentage = models.IntegerField()

    