from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Criteria(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='criteria_list')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
