from django.db import models
from django.contrib.auth.models import User
from accounts.enums import *


class JobSeeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    gender = models.PositiveSmallIntegerField(choices=GENDER)
    highest_education = models.IntegerField(choices=EDUCATION_QUALIFICATIONS)
    job_search_status = models.IntegerField(choices=JOB_SEARCH_STATUS)
    years_of_experiences = models.PositiveSmallIntegerField()
    monthly_expected_salary = models.PositiveIntegerField()
    resume = models.FileField(upload_to="resumes", null=True)