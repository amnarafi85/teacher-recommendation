from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('reviews.urls')),  # ✅ This makes sure that the `reviews` app's URLs are included
]
