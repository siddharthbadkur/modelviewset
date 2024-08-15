from .models import *
from rest_framework import serializers
from .serializers import *
from rest_framework import viewsets


class Studentviewset(viewsets.ModelViewSet):
 queryset = StudentModel.objects.all()
 serializer_class =StudentSerializer()
    
