# from django.contrib.auth import authenticate
# from django.contrib.auth.hashers import check_password
# from django.urls import reverse
# from django.contrib.auth.models import User
#
# import pytest
#
# @pytest.mark.django_db
# def test_login(web_client):
#     assert User.objects.count() == 0
#     User.objects.create_user(username="User", password="Password")
#     assert User.objects.count() == 1
#     post_data = {
#         'username': 'User',
#         'password': 'Password'
#     }
#     response = web_client.post(reverse('login'), post_data)
#     assert response.status_code == 302
#     assert authenticate(username='User', password='Password')
