from django.urls import path
from . import views

urlpatterns = [
    path('api/dealerships/', views.api_dealers),
    path('api/dealership/<int:pk>/', views.api_dealer_by_id),
    path('api/reviews/dealer/<int:dealer_id>/', views.api_reviews_for_dealer),
    path('api/login/', views.api_login),
    path('api/logout/', views.api_logout),
]
