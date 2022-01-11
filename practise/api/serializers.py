from rest_framework import serializers
from myapp.models import *


class ACModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ACModel
        fields = '__all__'


class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = ('id', 'serial_number', 'current_registration', 'model_id')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class WorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

