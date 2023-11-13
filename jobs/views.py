from rest_framework import generics
from jobs.serializers import JobPostSerializer
from jobs.models import JobPost, JobApplication


class JobPostListView(generics.ListAPIView):
    serializer_class = JobPostSerializer
    queryset = JobPost.objects.all()


class JobApplicationView(generics.ListAPIView):
    queryset = JobApplication.objects.all()  # TODO: need to add currently logged in user in the filter

