from django.urls import path
from .views import ReviewListCreateView, ApprovedReviewsListView, create_superuser  # ✅ Import create_superuser

urlpatterns = [
    path('reviews/', ReviewListCreateView.as_view(), name='reviews-list-create'),
    path('reviews/approved/', ApprovedReviewsListView.as_view(), name='approved-reviews'),
    path('create-superuser/', create_superuser),  # ✅ Add the new endpoint
]
