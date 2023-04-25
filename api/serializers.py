from rest_framework import serializers
from .models import Tile, Task


class TileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tile
        fields = ["_id", "name", "launch_date", "status", "created_at", "updated_at"]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "_id",
            "title",
            "order",
            "description",
            "type",
            "tile",
            "created_at",
            "updated_at",
        ]
