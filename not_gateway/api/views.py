from rest_framework import generics
from .models import Email
from .serializers import EmailSerializer


class EmailListCreateView(generics.ListCreateAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer


class EmailRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
