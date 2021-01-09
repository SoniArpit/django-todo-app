from rest_framework import viewsets
from ..models import Task
from .serializers import TodoSerailizer
from rest_framework.pagination import PageNumberPagination


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TodoSerailizer
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 10
