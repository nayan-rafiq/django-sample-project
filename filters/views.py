from rest_framework import generics
from filters.models import Category, Criteria
from filters.serializers import CategorySerializer


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    # prefetch is important, otherwise it'll execute one additional query per record
    queryset = Category.objects.prefetch_related('criteria_list')
    pagination_class = None

