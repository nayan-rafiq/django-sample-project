from django.urls import path

from . import views
from rest_framework import routers
from jobs.viewsets import EmployerViewSet

urlpatterns = [
    path("", views.JobPostListView.as_view()),
    path("applied", views.JobApplicationView.as_view()),
]

router = routers.SimpleRouter()
router.register(r'employers', EmployerViewSet)

urlpatterns += router.urls
