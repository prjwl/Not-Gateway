from django.urls import path
from .views import EmailListCreateView, EmailRetrieveUpdateDestroyView

urlpatterns = [
    path('email/', EmailListCreateView.as_view(), name='email-list-create'),
    path('email/<int:pk>/', EmailRetrieveUpdateDestroyView.as_view(), name='email-retrieve-update-destroy'),
]