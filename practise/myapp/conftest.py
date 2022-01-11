import pytest
from django.contrib.auth.models import User
from django.test import Client

from myapp.models import Task, Aircraft


@pytest.fixture
def web_client():
    client = Client()
    return client


@pytest.fixture
def new_Task():
    task = Task()
    task.id_number = '432345'
    task.description = 'Test1'
    task.model = '2'
    task.save()
    return task

@pytest.fixture
def new_user(web_client):
    user = User.objects.create_user(username="User", password='Password')
    web_client.force_login(user)
    return user

@pytest.fixture
def list_of_aircrafts():
    aircrafts = Aircraft.objects.all()
    return list(aircrafts)

def aircraft_create():
    aircraft = Aircraft()
    aircraft.serial_number = '776655'
    aircraft.current_registration = 'SP-WBC'
    aircraft.model_id = '2'
    aircraft.save()
    return aircraft
