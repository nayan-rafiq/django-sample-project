from django.urls import path

from accounts.api_views import JobSeekerProfileApiView, UploadResumeApiView

urlpatterns = [
    path("profile", JobSeekerProfileApiView.as_view()),
    path("resume", UploadResumeApiView.as_view()),
]
