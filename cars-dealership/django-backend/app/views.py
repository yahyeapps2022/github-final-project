from rest_framework import viewsets
from .models import Dealer, Review
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

# Minimal serializers inline for brevity
from rest_framework import serializers
class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

@api_view(['GET'])
def api_dealers(request):
    qs = Dealer.objects.all()
    return Response(DealerSerializer(qs, many=True).data)

@api_view(['GET'])
def api_dealer_by_id(request, pk):
    dealer = Dealer.objects.get(pk=pk)
    return Response(DealerSerializer(dealer).data)

@api_view(['GET'])
def api_reviews_for_dealer(request, dealer_id):
    reviews = Review.objects.filter(dealer_id=dealer_id)
    return Response(ReviewSerializer(reviews, many=True).data)

@api_view(['POST'])
def api_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return Response({'status':'ok','username':user.username})
    return Response({'status':'error'}, status=400)

@api_view(['POST'])
def api_logout(request):
    logout(request)
    return Response({'status':'ok'})
