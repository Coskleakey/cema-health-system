from django.urls import path
from .views import ClientListView, ClientDetailView, ProgramListView

urlpatterns = [
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('programs/', ProgramListView.as_view(), name='program-list'),
]
