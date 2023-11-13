from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.authentication import SessionAuthentication

from accounts.serializers import JobSeekerProfileSerializer, UploadResumeSerializer
from accounts.models import JobSeeker


class JobSeekerProfileApiView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        """
        Returns the JobSeeker profile for current user. Returns a 404 if user has created no profile yet
        """
        job_seeker_profile = JobSeeker.objects.filter(user=request.user).first()
        if job_seeker_profile is None:
            return Response({"message": "profile not found"})
        else:
            serializer = JobSeekerProfileSerializer(job_seeker_profile)
            return Response(serializer.data)

    def post(self, request):
        job_seeker_profile = JobSeeker.objects.filter(user=request.user).first()
        serializer = JobSeekerProfileSerializer(job_seeker_profile, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class UploadResumeApiView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [CsrfExemptSessionAuthentication, ]

    def post(self, request):
        try:
            job_seeker_profile = JobSeeker.objects.get(user=request.user)
        except JobSeeker.DoesNotExist:
            raise NotFound(detail="Profile not found")

        serializer = UploadResumeSerializer(job_seeker_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)