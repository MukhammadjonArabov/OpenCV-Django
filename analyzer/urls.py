from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("camera/", views.camera_view, name="camera"),
    path("analyze_image/", views.analyze_image, name="analyze_image"),
]
