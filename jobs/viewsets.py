from jobs.serializers import EmployerSerializer
from jobs.models import Employer
from rest_framework import viewsets
from rest_framework import filters


class EmployerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This view set can be used to get a list of employers and a specific employer
    """
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    filter_backends = [filters.SearchFilter,]
    filter_fields = ['name',]