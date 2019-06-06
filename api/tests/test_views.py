from django.test import TestCase, Client
from rest_framework import status
from api.models import Company, Review
from api.views.auth import login, logout
from api.views.generic_cbv import ReviewList, CompanyList
from django.contrib.auth.models import User
from django.http import HttpResponse

class TestGenericsViews(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            id = '5',
            username='test_user',
            email = 'bashenov98@inbox.ru',
        )
        password = '123456'
        self.user1.set_password(password)
        self.user1.save()
        self.client = Client()
        self.client.login(username = self.user1.username, password=password)
        self.company1 = Company.objects.create(
            id = '9',
            name='test_company',
            bio='testing',
        )


    def test_company_list_get_queryset(self):
        response = self.client.get('http://127.0.0.1:8000/api/companies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_company_perform_create(self):
        response2 = self.client.post('http://127.0.0.1:8000/api/companies/',{'id':"8",'name':"test_company", 'bio':"test_bio"})
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)

    def test_review_list_get_queryset(self):
        response3 = self.client.get('http://127.0.0.1:8000/api/reviews/')
        self.assertEqual(response3.status_code, status.HTTP_200_OK)

    def test_review_perform_create(self):

        response4 = self.client.post('http://127.0.0.1:8000/api/reviews/',{'title':"test_review", 'rating':"5",
                                                                           'ip_address':"123.123.123.123",'summary':"testing",
                                                                          'submission_date':"2018-07-07",'company':self.company1.id, 'created_by':self.user1})
        self.assertEqual(response4.status_code, status.HTTP_201_CREATED)


class TestLogin(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            username='test_user',
            email = 'bsahenov@mail.ru',
            password = '123456',
            )
        # password = '123456'
        # self.user1.set_password(password)
        self.user1.save()
        self.client = Client()

    def test_login(self):
        response = self.client.post('http://127.0.0.1:8000/api/login/',{'username': "test_user", 'password': "123456"})
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

#
# class TestLogout(TestCase):
#     def setUp(self):
#         self.user1 = User.objects.create(
#             id='5',
#             username='test_user',
#             email='bashenov98@inbox.ru',
#         )
#         password = '123456'
#         self.user1.set_password(password)
#         self.user1.save()
#         self.client = Client()
#         self.client.login(username=self.user1.username, password=password)
#
#     def test_logout(self):
#         response = self.client.post()
#
#
#




