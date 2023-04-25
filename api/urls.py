from django.urls import path
from .views import health_check, TileViewSet, TaskViewSet

tile_list = TileViewSet.as_view({"get": "list", "post": "create"})
tile_detail = TileViewSet.as_view(
    {"get": "retrieve", "delete": "destroy", "patch": "partial_update"}
)
task_list = TaskViewSet.as_view({"get": "list", "post": "create"})
task_detail = TaskViewSet.as_view({"get": "retrieve", "delete": "destroy"})

urlpatterns = [
    path("check", health_check, name="health_check"),
    path("tiles/", tile_list, name="tiles-list"),
    path("tiles/<int:pk>/", tile_detail, name="tiles-detail"),
    path("tasks/", task_list, name="tasks-list"),
    path("tasks/<int:pk>/", task_detail, name="tasks-detail"),
]
