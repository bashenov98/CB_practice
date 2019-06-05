from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=20)
    bio = models.TextField(max_length=1000)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)


class Review(models.Model):
    title = models.CharField(max_length=35)
    rating = models.IntegerField(range(1,5),)
    ip_address = models.CharField(max_length=20)
    summary = models.CharField(max_length=300, default=1)
    submission_date = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return '{}: {}'.format(self.id, self.title)


