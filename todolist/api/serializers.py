from rest_framework import serializers
from ..models import Task


class TodoSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
