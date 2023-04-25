from django.db import models

# Create your models here.
class Tile(models.Model):
    class TileStatusType(models.TextChoices):
        LIVE = "L", "Live"
        PENDING = "P", "Pending"
        ARCHIVED = "A", "Archived"

    _id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    launch_date = models.DateTimeField()
    status = models.CharField(
        max_length=1, choices=TileStatusType.choices, default=TileStatusType.LIVE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Task(models.Model):

    _id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    order = models.TextField()
    description = models.TextField()
    type = models.CharField(max_length=55)
    tile = models.ForeignKey(Tile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
