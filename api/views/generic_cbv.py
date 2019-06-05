from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.models import Review, Company
from api.serializers import ReviewSerializer, CompanySerializer

class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Review.objects.filter(created_by = self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by= self.request.user)


class CompanyList(generics.ListCreateAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        return Company.objects.all()

    def perform_create(self, serializer):
        serializer.save()






