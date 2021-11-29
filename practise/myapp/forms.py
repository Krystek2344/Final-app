from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from myapp.models import (Aircraft,
                          WorkOrder,
                          ACModel,
                          Task,
                          Customer,
                          WorkContent,)

class AddWorkContentForm(forms.ModelForm):
    class Meta:
        model = WorkContent
        fields = '__all__'


class AddCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class AddAircraftModelForm(forms.ModelForm):
    class Meta:
        model = ACModel
        fields = '__all__'


class AddAircraftForm(forms.ModelForm):
    class Meta:
        model = Aircraft
        fields = '__all__'


class AddWorkOrderForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
