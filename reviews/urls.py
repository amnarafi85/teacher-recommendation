from django.urls import path
from .views import ReviewListCreateView, ApprovedReviewsListView

urlpatterns = [
    path('reviews/', ReviewListCreateView.as_view(), name='reviews-list-create'),  # Existing endpoint
    path('reviews/approved/', ApprovedReviewsListView.as_view(), name='approved-reviews'),
    path('create-superuser/', create_superuser),# ✅ New endpoint for approved reviews
]
