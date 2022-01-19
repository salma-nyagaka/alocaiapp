from django.urls import include, path

from .views import DatabaseConnectionApiView

urlpatterns = [
    path("status", DatabaseConnectionApiView.as_view(),
         name="database-connection"),
]
