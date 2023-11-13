from rest_framework import serializers
from filters.models import Category, Criteria


class CriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criteria
        exclude = ('category',)


class CategorySerializer(serializers.ModelSerializer):
    criteria_list = CriteriaSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'criteria_list', )
