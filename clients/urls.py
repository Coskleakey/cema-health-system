from django.urls import path
from .views import client_list, register_client, enroll_client, client_profile

urlpatterns = [
    path('', client_list, name='client-list'),
    path('register/', register_client, name='register-client'),
    path('enroll/', enroll_client, name='enroll-client'),
    path('<int:client_id>/', client_profile, name='client-profile'),
]
