from django.test import TestCase
from api.models import Review, Company
from django.contrib.auth.models import User

class TestModels(TestCase):
    def setUp(self):
        self.company1 = Company.objects.create(
            name = 'test_company',
            bio = 'testing',
        )
        self.user1 = User.objects.create(
            username = 'test_user',
            password = '123456'
        )
        self.review1 = Review.objects.create(
            title = 'test_review',
            rating = 2,
            ip_address = '123.123.123.123',
            summary = 'test_summary',
            submission_date = '2018-05-05',
            company = self.company1,
            created_by = self.user1
        )

    def test_review_can_be_str(self):
        self.assertEqual(str(self.review1), '{}: {}'.format(self.review1.id, self.review1.title))

    def test_company_can_be_str(self):
        self.assertEqual(str(self.company1), '{}: {}'.format(self.company1.id, self.company1.name))