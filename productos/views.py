from django.shortcuts import render
from rest_framework import viewsets
from .models import Chela
from .serializers import ChelaSerializer
from django.http import HttpResponse
class ChelaViewSet(viewsets.ModelViewSet):
    serializer_class = ChelaSerializer
    queryset = Chela.objects.all()

    
def index(request):
    return HttpResponse("index")