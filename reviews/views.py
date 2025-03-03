from rest_framework import viewsets, generics
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.permissions import AllowAny

# ✅ View to retrieve only approved reviews
class ApprovedReviewsListView(generics.ListAPIView):  
    queryset = Review.objects.filter(approved=True)  # Only fetch approved reviews
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]  # Public access to view approved reviews

# ✅ View to list all reviews and create new ones
class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
from django.http import HttpResponse
from django.contrib.auth.models import User

