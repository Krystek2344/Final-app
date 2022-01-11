from rest_framework import generics
from myapp.models import *
from .serializers import *


class ACModelListView(generics.ListAPIView):
    queryset = ACModel.objects.all()
    serializer_class = ACModelSerializer


class ACModelDetailView(generics.RetrieveAPIView):
    queryset = ACModel.objects.all()
    serializer_class = ACModelSerializer


class AircraftListView(generics.ListAPIView):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer


class AircraftDetailView(generics.RetrieveAPIView):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer

