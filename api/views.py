from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Tile, Task
from .serializers import TileSerializer, TaskSerializer
from .renderer import APIRenderer

# Create your views here.
@api_view(["GET"])
def health_check(request):
    return Response({"success": True}, 200)

class TileViewSet(viewsets.ModelViewSet):
    queryset = Tile.objects.all()
    serializer_class = TileSerializer
    renderer_classes = [APIRenderer]
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    renderer_classes = [APIRenderer]
