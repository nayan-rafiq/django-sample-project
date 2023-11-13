from django.db import models
from .enums import *
from filters.models import Criteria
from accounts.models import JobSeeker


class Employer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class JobPost(models.Model):
    title = models.CharField(max_length=500)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateField(null=True)


class JobPostTag(models.Model):
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    tag = models.ForeignKey(Criteria, on_delete=models.CASCADE)


class JobApplication(models.Model):
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(choices=JOB_APPLICATION_STATUS)
