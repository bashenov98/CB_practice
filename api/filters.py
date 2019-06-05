from django_filters import rest_framework as filters
from api.models import Review

class ReviewFilter(filters.FilterSet):
    rating = filters.NumberFilter()
    title = filters.CharFilter()
    summary = filters.CharFilter()
    ip_address = filters.CharFilter()
    submission_date = filters.DateFilter()

    class Meta:
        model = Review
        fields = ('rating', 'title', 'submissionDate')

