from django.urls import path
from api import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('reviews/', views.ReviewList.as_view()),
    path('companies/', views.CompanyList.as_view()),
]