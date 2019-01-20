from django.urls import path
from .views import DeckView, ListCardView

urlpatterns = [
    path('cards/', ListCardView.as_view(), name="cards-all"),
    path('deck/create', DeckView.as_view())
]