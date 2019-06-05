from rest_framework import serializers
from api.models import Review, Company
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class CompanySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    bio = serializers.CharField()

    class Meta:
        model = Company
        fields = '__all__'

    def create(self, validated_data):
        company = Company(**validated_data)
        company.save()
        return company


class ReviewSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    rating = serializers.IntegerField()
    ip_address = serializers.CharField()
    summary = serializers.CharField()
    submission_date = serializers.DateField()
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'

    def create(self, validated_data):
        review = Review(**validated_data)
        review.save()
        return review