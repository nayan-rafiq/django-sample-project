from rest_framework import serializers
from accounts.models import JobSeeker


class JobSeekerProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobSeeker
        exclude = ('user', )
        read_only_fields = ['resume', ]


class UploadResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeeker
        fields = ['resume', ]
