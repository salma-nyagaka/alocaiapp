from django.urls import include, path

from .views import GamesApiView, PenDriveApiView

urlpatterns = [
    path("games", GamesApiView.as_view(), name="create-game"),
    path('best_value_games', PenDriveApiView.as_view(),
    name='best-value-game'),
]
