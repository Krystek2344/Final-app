from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.urls import reverse
from django.contrib.auth.models import User

import pytest


@pytest.mark.django_db
def test_add_user(web_client):
    assert User.objects.count() == 0
    username = "Bobi"
    email = "bill@gmail.com"
    password = "hasło1234"
    first_name = 'Bob',
    post_data = {
        'username': username,
        'email': email,
        'password': password,
        'first_name': first_name,
    }

    response = web_client.post(reverse('registration'), post_data)

    assert User.objects.count() == 1
    user = User.objects.first()
    assert user.username == username
    assert user.email == email
    assert check_password(encoded=user.password, password=password)


@pytest.mark.django_db
def test_login(web_client):
    assert User.objects.count() == 0
    User.objects.create_user(username="User", password="Password")
    assert User.objects.count() == 1
    post_data = {
        'username': 'User',
        'password': 'Password'
    }
    response = web_client.post(reverse('login'), post_data)
    assert response.status_code == 302
    assert authenticate(username='User', password='Password')


@pytest.mark.django_db
def test_home_view(client):
    response = client.get(reverse('home'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_aircrafts_view(client, aircrafts_list):
    response = client.get('/aircraft_list')
    assert response.status_code == 200
    aircrafts = response.context['aircrafts']
    assert list(aircrafts) == aircrafts_list
