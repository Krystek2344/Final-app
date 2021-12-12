from django.contrib.auth import authenticate
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.test import Client, TestCase
from myapp.models import Aircraft, Task

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
    response = web_client.post(reverse('register_user'), post_data)
    assert response.status_code == 302
    assert User.objects.count() == 1
    assert User.objects.first().username == post_data['login']


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


# @pytest.mark.django_db
# def test_aircrafts_view(client, list_of_aircrafts):
#     response = client.get('/aircraft_list')
#     assert response.status_code == 301
#     aircrafts = response.context['aircrafts']
#     assert list(aircrafts) == list_of_aircrafts


@pytest.mark.django_db
def test_logout(client, new_user):
    assert new_user.is_authenticated
    response = client.get(reverse('logout'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_login_view(client):
    assert User.objects.count() == 0
    User.objects.create_user(username='Test_username', password='Test_password')
    assert User.objects.count() == 1
    post_data = {
        'username': 'Test_username',
        'password': 'Test_password'
    }
    response = client.post(reverse('login'), post_data)
    assert response.status_code == 302
    assert authenticate(username='Test_username', password='Test_password')
