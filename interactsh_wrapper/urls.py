from django.urls import path
from .views import GetURLView, GetInteractionsView

urlpatterns = [
    path('getURL/', GetURLView.as_view(), name='get_url'),
    path('getInteractions/', GetInteractionsView.as_view(), name='get_interactions'),
]
