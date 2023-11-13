from rest_framework import serializers
from jobs.models import Employer, JobPost


class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        exclude = ()


class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        exclude = ()
